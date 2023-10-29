from django.shortcuts import render

from django.http import HttpResponse

class Recipe:
  def __init__(self, name, cuisine, time, feeds):
    self.name = name
    self.cuisine = cuisine
    self.time = time
    self.feeds = feeds

recipes= [
  Recipe('Pizza', 'American', '1 Hour', '4'),
  Recipe('Burger', 'American', '1 Hour', '4'),
  Recipe('Cookie', 'American', '1 Hour', '1'),
  Recipe('Popcorn', 'American', '1 Hour', '2')
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Recipe Organizer Home Page</h1>')

def about(request):
  return render(request, 'about.html')

def recipe_index(request):
  return render(request, 'recipes/index.html', {'recipes': recipes})