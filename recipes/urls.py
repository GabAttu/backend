# recipes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_recipes, name='search_recipes'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('profile/', views.profile, name='profile'),
    path('favorites/', views.favorite_recipes, name='favorite_recipes'),
    path('login_and_registration/', views.login_and_registration, name='login_and_registration'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),
]
