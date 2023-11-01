from django.contrib import admin

# Register your models here.
from .models import Recipe, CookingEvent, Ingredient

admin.site.register(Recipe)
admin.site.register(CookingEvent)
admin.site.register(Ingredient)