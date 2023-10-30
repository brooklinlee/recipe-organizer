from django.shortcuts import render
from .models import Recipe

from django.http import HttpResponse

# class Recipe:
#   def __init__(self, name, cuisine, time, feeds):
#     self.name = name
#     self.cuisine = cuisine
#     self.time = time
#     self.feeds = feeds

# recipes= [
#   Recipe('Pizza', 'American', '1 Hour', '4'),
#   Recipe('Burger', 'American', '1 Hour', '4'),
#   Recipe('Cookie', 'American', '1 Hour', '1'),
#   Recipe('Popcorn', 'American', '1 Hour', '2')
# ]

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
  return render(request, 'recipes/detail.html', { 'recipe': recipe })