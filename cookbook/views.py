from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Recipe, RecipeIngredient

class HomeView(ListView):
	model = Recipe
	template_name = 'home.html'

class RecipeDetailView(DetailView):
	model = Recipe
	template_name = 'recipe_detail.html'


#class AddRecipeView(CreateView):
#	model = Recipe
#	template_name = 'add_recipe.html'
#	fields = '__all__'

# Create your views here.
