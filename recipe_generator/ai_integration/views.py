from django.shortcuts import render, redirect
from .forms import RecipePromptForm
import openai
import pyttsx3
import json

from django.contrib import messages
from recipes.models import Recipe
from django.contrib.auth.decorators import login_required


# Load your OpenAI API key securely
import os
from dotenv import load_dotenv
load_dotenv()
# Correct API key loading method
api_key = os.getenv("OPENAI_API_KEY")

# Ensure the key is loaded
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY is missing or not loaded correctly.")

client = openai.Client(api_key=api_key)
# 🚨 AI Recipe Generation Logic
def generate_few_shot_recipe_chat(user_prompt: str) -> dict:
    client = openai.Client()

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful chef AI assistant. "
                "You should respond in valid JSON with the keys: "
                "title, ingredients, instructions, and estimated_time."
            )
        },
        {"role": "user", "content": user_prompt}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=400,
            temperature=0.7,
        )

        # ✅ Ensure JSON response is parsed correctly
        recipe_data = json.loads(response.choices[0].message.content.strip())
        return recipe_data

    except Exception as e:
        return {"error": f"Failed to generate recipe: {str(e)}"}
# 🚨 TTS Logic

def tts_offline_colab(text: str, filename="recipe_audio.mp3"):
    engine = pyttsx3.init()

    # Save inside ai_integration folder
    audio_path = os.path.join(os.path.dirname(__file__), filename)
    engine.save_to_file(text, audio_path)
    engine.runAndWait()

    # Return a relative URL path for HTML
    return f"/ai_integration/{filename}"  # URL path to access the file


def generate_recipe(request):
    if request.method == 'POST':
        form = RecipePromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            recipe_data = generate_few_shot_recipe_chat(prompt)

            if isinstance(recipe_data, str):
                try:
                    recipe_data = json.loads(recipe_data)
                except json.JSONDecodeError:
                    messages.error(request, "Error decoding recipe data.")
                    return render(request, 'ai_integration/generate_recipe.html', {'form': form})

            if isinstance(recipe_data.get("instructions"), str):
                recipe_data["instructions"] = recipe_data["instructions"].split("\n")

            # 📦 Nutritional breakdown logic
            ingredients_text = ', '.join(recipe_data.get('ingredients', []))
            nutrition_prompt = f"Give a nutritional breakdown (calories, protein, fat, carbs) for these ingredients: {ingredients_text}"

            nutrition_response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful nutritional assistant."},
                    {"role": "user", "content": nutrition_prompt}
                ],
                max_tokens=300,
                temperature=0.6
            )

            recipe_data["nutrition"] = nutrition_response.choices[0].message.content.strip()

            # Text-to-Speech
            recipe_text = (
                f"{recipe_data['title']}\nIngredients: {ingredients_text}\n"
                f"Instructions: {', '.join(recipe_data['instructions'])}\n"
                f"Estimated Time: {recipe_data['estimated_time']}"
            )
            audio_file = tts_offline_colab(recipe_text)

            return render(request, 'ai_integration/generated_recipe.html', {
                'recipe': recipe_data,
                'audio_file': audio_file
            })
    else:
        form = RecipePromptForm()

    return render(request, 'ai_integration/generate_recipe.html', {'form': form})


@login_required
def save_ai_recipe(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')

        Recipe.objects.create(
            user=request.user,
            title=title,
            ingredients=ingredients,
            instructions=instructions
        )
        messages.success(request, "✅ AI recipe saved successfully!")
        return redirect('dashboard')
    return redirect('generate_recipe')

