from django.shortcuts import render, redirect
from .models import Recipe, Ingredient
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CookingEventForm
from django.views.generic import ListView, DetailView

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def recipe_index(request):
  recipes = Recipe.objects.all()
  return render(request, 'recipes/index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
  recipe = Recipe.objects.get(id=recipe_id)
  ingredients_recipe_doesnt_have = Ingredient.objects.exclude(id__in = recipe.ingredients.all().values_list('id'))
  cooking_event_form = CookingEventForm()
  return render(request, 'recipes/detail.html', { 'recipe': recipe, 'cooking_event_form': cooking_event_form, 'ingredients': ingredients_recipe_doesnt_have })

class RecipeCreate(CreateView):
  model = Recipe
  fields = ['name', 'cuisine', 'time', 'feeds', 'recipe']

class RecipeUpdate(UpdateView):
  model = Recipe
  fields = '__all__'

class RecipeDelete(DeleteView):
  model = Recipe
  success_url = '/recipes/'

def add_cooking_event(request, recipe_id):
  form = CookingEventForm(request.POST)
  if form.is_valid():
    new_cooking_event = form.save(commit=False)
    new_cooking_event.recipe_id = recipe_id
    new_cooking_event .save()
  return redirect('recipe-detail', recipe_id=recipe_id)

class IngredientCreate(CreateView):
  model = Ingredient
  fields = '__all__'

class IngredientList(ListView):
  model = Ingredient

class IngredientDetail(DetailView):
  model = Ingredient

class IngredientUpdate(UpdateView):
  model = Ingredient
  fields = ['name', 'food_group']

class IngredientDelete(DeleteView):
  model = Ingredient
  success_url = '/ingredients'

def assoc_ingredient(request, recipe_id, ingredient_id):
  Recipe.objects.get(id=recipe_id).ingredients.add(ingredient_id)
  return redirect('recipe-detail', recipe_id=recipe_id)
