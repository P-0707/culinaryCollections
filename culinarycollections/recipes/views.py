from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category, Collection

def home(request):
    recipes = Recipe.objects.all()[:6]  # Fetch a few recipes to feature
    categories = Category.objects.all()  # Fetch all categories
    collections = Collection.objects.all()  # Fetch all collections
    return render(request, 'recipes/main/home.html', {
        'recipes': recipes,
        'categories': categories,
        'collections': collections
    })

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/main/recipe_detail.html', {'recipe': recipe})

# View to filter recipes by category
def category_recipes(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'recipes/main/category_recipes.html', {'category': category, 'recipes': recipes})

# View to filter recipes by collection
def collection_recipes(request, collection_name):
    collection = get_object_or_404(Collection, title=collection_name)
    recipes = Recipe.objects.filter(collection=collection)
    return render(request, 'recipes/main/collection_recipes.html', {'collection': collection, 'recipes': recipes})

def search_results(request):
    query = request.GET.get('q')
    recipes = Recipe.objects.filter(title__icontains=query)  # Search for recipes by title
    return render(request, 'recipes/main/search_results.html', {'recipes': recipes, 'query': query})

