from django import forms

class RecipePromptForm(forms.Form):
    prompt = forms.CharField(
        label='Describe your ingredients or desired recipe',
        max_length=200,
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g. "I have chicken and rice."'})
    )
