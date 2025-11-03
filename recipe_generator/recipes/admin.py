from django.contrib import admin
from .models import Recipe, StandardRecipe

# Unregister first to avoid AlreadyRegistered error
try:
    admin.site.unregister(StandardRecipe)
except admin.sites.NotRegistered:
    pass

@admin.register(StandardRecipe)
class StandardRecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'cuisine_type', 'meal_type']

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at']
