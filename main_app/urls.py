from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('recipes/', views.recipe_index, name='recipe-index'),
  path('recipes/<int:recipe_id/', views.recipe_detail, name='recipe-detail')
]
