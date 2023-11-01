from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Ingredient(models.Model):
  name = models.CharField(max_length=50)
  FOOD_GROUP_CHOICES = [
    ('fruit', 'Fruit'),
    ('vegetable', 'Vegetable'),
    ('grain', 'Grain'),
    ('protein', 'Protien'),
    ('dairy', 'Dairy'),
    ('sugar', 'Sugar'),
  ]
  food_group = models.CharField(
    max_length=30,
    choices=FOOD_GROUP_CHOICES,
    default=FOOD_GROUP_CHOICES[0][0]
  )
  

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('ingredient-detail', kwargs={'pk': self.id})


class Recipe(models.Model):
  name = models.CharField(max_length=100)
  CUISINE_CHOICES = [
    ('american', 'American'),
    ('italian', 'Italian'),
    ('mexican', 'Mexican'),
    ('indian', 'Indian'),
    ('asian', 'Asian'),
    ('other', 'Other'),
  ]
  TIME_CHOICES = [
    ('30 Minutes', '30 Minutes'),
    ('1 Hour', '1 Hour'),
    ('1.5 Hours', '1.5 Hours'),
    ('2 Hours', '2 Hours'),
    ('2.5 Hours', '2.5 Hours'),
    ('Up to 6 Hours', 'Up to 6 Hours'),
    ('More than 6 Hours', 'More than 6 Hours'),
  ]
  cuisine = models.CharField(
    max_length=20,
    choices=CUISINE_CHOICES,
    default=CUISINE_CHOICES[0][0]
  )
  time = models.CharField(
    max_length = 50,
    choices=TIME_CHOICES,
    default=TIME_CHOICES[0][0]
  )
  feeds = models.IntegerField()
  recipe = models.TextField(max_length = 500)
  ingredients = models.ManyToManyField(Ingredient)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('recipe-detail', kwargs={'recipe_id': self.id})
  
class CookingEvent(models.Model):
  date = models.DateField('Cooking Event Date')
  notes = models.CharField(max_length = 255)

  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='cooking_events')

  def __str__(self):
    return f"{self.recipe} on {self.date}"
  
  class Meta:
    ordering = ['-date']