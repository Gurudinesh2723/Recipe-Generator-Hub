from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_recipe, name='create_recipe'),
    path('view/', views.view_past_recipes, name='view_past_recipes'),
    path('edit/<int:id>/', views.edit_recipe, name='edit_recipe'),
    path('delete/<int:id>/', views.delete_recipe, name='delete_recipe'),
    path('standard-recipes/', views.view_standard_recipes, name='view_standard_recipes'),

]
