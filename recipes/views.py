from django.http import HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm, RegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import LoginForm
from .forms import RecipeForm

def home(request):
    top_recipes = Recipe.objects.order_by('-likes')[:5]  # Mostra le prime 5 ricette con più mi piace

    context = {
        'top_recipes': top_recipes,
    }
    return render(request, 'recipes/home.html', context)
def search_recipes(request):
    query = request.GET.get('query')
    recipes = Recipe.objects.all()

    if query:
        recipes = recipes.filter(title__icontains=query)

    return render(request, 'recipes/search_results.html', {'recipes': recipes, 'query': query})

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm

@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/create_recipe.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    liked_recipes = user.liked_recipes.all()
    context = {
        'liked_recipes': liked_recipes,
    }
    return render(request, 'recipes/profile.html', context)


@login_required
def favorite_recipes(request):
    user = request.user
    liked_recipes = user.liked_recipes.all()
    return render(request, 'recipes/favorite_recipes.html', {'liked_recipes': liked_recipes})
def login_and_registration(request):
    if request.user.is_authenticated:
        return redirect('home')  # Reindirizza alla home se l'utente è già autenticato

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Reindirizza alla home dopo il login
    else:
        login_form = LoginForm()

    registration_form = RegistrationForm()

    context = {
        'login_form': login_form,
        'registration_form': registration_form,
    }
    return render(request, 'recipes/login_and_registration.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')

# recipes/views.py

from django.shortcuts import render, get_object_or_404
from .models import Recipe


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user in recipe.likes.all():
                recipe.likes.remove(request.user)
            else:
                recipe.likes.add(request.user)
        else:
            return redirect('login_and_registration')  # Reindirizza l'utente non autenticato alla pagina di login

    context = {
        'recipe': recipe,
    }
    return render(request, 'recipes/recipe_detail.html', context)


def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Reindirizza al profilo dopo la modifica
    else:
        form = RecipeForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'recipes/edit_recipe.html', context)

@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user != recipe.author:
        return HttpResponseForbidden()
    if request.method == 'POST':
        recipe.delete()
        return redirect('profile')


def like_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        # Aggiungi l'utente corrente ai preferiti della ricetta
        if recipe.favorites.filter(id=request.user.id).exists():
            # Se l'utente è già tra i preferiti, non fare nulla
            pass
        else:
            recipe.favorites.add(request.user)
            recipe.likes += 1
            recipe.save()
    return redirect('recipe_detail', pk=recipe_id)


def favorite_recipes(request):
    user = request.user
    favorite_recipes = user.favorite_recipes.all()
    return render(request, 'recipes/favorite_recipes.html', {'recipes': favorite_recipes})

