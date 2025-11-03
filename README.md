# 🧑‍🍳 Recipe Generator Hub

Welcome to **Recipe Generator Hub** — an AI-powered Django web app that helps users generate custom recipes using OpenAI, manage saved recipes, and enjoy a personalized cooking experience.

---

## 🚀 Features

- 🧠 **AI-Powered Recipe Generation** (via OpenAI)
- 📝 **Register & Login** for personalized experience
- 📜 **View Past Recipes** in your dashboard
- ➕ **Create Your Own Recipes**
- 📚 **Explore Standard Recipes** by cuisine & meal type (e.g., Continental Dinner, Asian Breakfast, etc.)
- 🤖 **AI Recipe Generator** interface
- 🧼 Clean UI/UX with modern components

---

## 🧰 Tech Stack

- **Backend**: Django
- **Frontend**: HTML5, CSS3
- **AI Integration**: OpenAI API
- **Database**: SQLite3 (default Django DB)
- **Authentication**: Django built-in auth system

---

## 🛠️ Setup Instructions

### 1⃣ Clone the Repository

```bash
git clone https://github.com/Gurudinesh2723/Recipe-Generator-Hub.git
cd Recipe-Generator-Hub/recipe_generator
```

### 2⃣ Set Up Virtual Environment & Install Dependencies

```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
source env/bin/activate      # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3⃣ Apply Migrations and Start the Server

```bash
python manage.py migrate
python manage.py runserver
```

Visit the app at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
