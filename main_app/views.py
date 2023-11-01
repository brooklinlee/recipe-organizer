from django.shortcuts import render, redirect
from .models import Recipe, Ingredient
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CookingEventForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def recipe_index(request):
  recipes = Recipe.objects.filter(user=request.user)
  return render(request, 'recipes/index.html', {'recipes': recipes})

@login_required
def recipe_detail(request, recipe_id):
  recipe = Recipe.objects.get(id=recipe_id)
  ingredients_recipe_doesnt_have = Ingredient.objects.exclude(id__in = recipe.ingredients.all().values_list('id'))
  cooking_event_form = CookingEventForm()
  return render(request, 'recipes/detail.html', { 'recipe': recipe, 'cooking_event_form': cooking_event_form, 'ingredients': ingredients_recipe_doesnt_have })


class RecipeCreate(LoginRequiredMixin, CreateView):
  model = Recipe
  fields = ['name', 'cuisine', 'time', 'feeds', 'recipe']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RecipeUpdate(LoginRequiredMixin, UpdateView):
  model = Recipe
  fields = '__all__'

class RecipeDelete(LoginRequiredMixin, DeleteView):
  model = Recipe
  success_url = '/recipes/'

@login_required
def add_cooking_event(request, recipe_id):
  form = CookingEventForm(request.POST)
  if form.is_valid():
    new_cooking_event = form.save(commit=False)
    new_cooking_event.recipe_id = recipe_id
    new_cooking_event .save()
  return redirect('recipe-detail', recipe_id=recipe_id)

class IngredientCreate(LoginRequiredMixin, CreateView):
  model = Ingredient
  fields = '__all__'

class IngredientList(LoginRequiredMixin, ListView):
  model = Ingredient

class IngredientDetail(LoginRequiredMixin, DetailView):
  model = Ingredient

class IngredientUpdate(LoginRequiredMixin, UpdateView):
  model = Ingredient
  fields = ['name', 'food_group']

class IngredientDelete(LoginRequiredMixin, DeleteView):
  model = Ingredient
  success_url = '/ingredients'

@login_required
def assoc_ingredient(request, recipe_id, ingredient_id):
  Recipe.objects.get(id=recipe_id).ingredients.add(ingredient_id)
  return redirect('recipe-detail', recipe_id=recipe_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cat-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
