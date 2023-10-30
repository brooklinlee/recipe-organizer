from django.db import models

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
    default='american'
  )
  time = models.IntegerField()
  feeds = models.IntegerField()
  recipe = models.TextField(max_length = 500)
  
  def __str__(self):
    return self.name