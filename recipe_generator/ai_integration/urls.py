from django.urls import path
from . import views

urlpatterns = [
    path('generate-recipe/', views.generate_recipe, name='generate_recipe'),
    path('save-ai-recipe/', views.save_ai_recipe, name='save_ai_recipe'),
]
