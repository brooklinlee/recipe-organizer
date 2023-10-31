from django.db import models
from django.urls import reverse

# Create your models here.
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
  cuisine = models.CharField(
    max_length=20,
    choices=CUISINE_CHOICES,
    default=CUISINE_CHOICES[0][0]
  )
  time = models.IntegerField()
  feeds = models.IntegerField()
  recipe = models.TextField(max_length = 500)
  
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