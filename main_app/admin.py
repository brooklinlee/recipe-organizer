from django.contrib import admin

# Register your models here.
from .models import Recipe, CookingEvent

admin.site.register(Recipe)
admin.site.register(CookingEvent)