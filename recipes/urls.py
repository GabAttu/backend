# recipes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_recipes, name='search_recipes'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('profile/', views.profile, name='profile'),
    path('login_and_registration/', views.login_and_registration, name='login_and_registration'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:pk>/like/', views.like_recipe, name='like_recipe'),
    path('favorites/', views.favorite_recipes, name='favorite_recipes'),
    path('recipe/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('recipe/delete/<int:recipe_id>/', views.recipe_delete, name='recipe_delete'),
]