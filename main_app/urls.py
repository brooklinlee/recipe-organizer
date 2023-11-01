from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('recipes/', views.recipe_index, name='recipe-index'),
  path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe-detail'),
  path('recipes/create/', views.RecipeCreate.as_view(), name='recipe-create'),
  path('recipes/<int:pk>/update', views.RecipeUpdate.as_view(), name='recipe-update'),
  path('recipes/<int:pk>/delete', views.RecipeDelete.as_view(), name='recipe-delete'),
  path('recipes/<int:recipe_id>/add-cooking-event/', views.add_cooking_event, name='add-cooking-event'),
  path('recipes/<int:recipe_id>/assoc-ingredient/<int:ingredient_id>/', views.assoc_ingredient, name='assoc-ingredient'),
  path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredient-create'),
  path('ingredients/<int:pk>/', views.IngredientDetail.as_view(), name='ingredient-detail'),
  path('ingredients/', views.IngredientList.as_view(), name='ingredient-index'),
  path('ingredients/<int:pk>/update', views.IngredientUpdate.as_view(), name='ingredient-update'),
  path('ingredients/<int:pk>/delete', views.IngredientDelete.as_view(), name='ingredient-delete'),
  path('accounts/signup/', views.signup, name='signup'),
]
