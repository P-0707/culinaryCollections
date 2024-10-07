from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),  # Single recipe detail
    path('category/<str:category_name>/', views.category_recipes, name='category_recipes'),  # Recipes by category
    path('collection/<str:collection_name>/', views.collection_recipes, name='collection_recipes'),  # Recipes by collection
    path('search/', views.search_results, name='search_results'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)