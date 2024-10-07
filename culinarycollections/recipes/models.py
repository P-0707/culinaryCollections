from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# Model for Recipe Categories
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for Recipe Collections
class Collection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

# Model for Recipes
class Recipe(models.Model):

    TITLE_CHOICES = [
        ('veg', 'Vegetarian'),
        ('non_veg', 'Non-Vegetarian'),
        ('vegan', 'Vegan'),
    ]

    title = models.CharField(max_length=200)
    description = RichTextField()  # Enhanced text field for description
    ingredients = RichTextField()   # Enhanced text field for ingredients
    instructions = RichTextField()   # Enhanced text field for instructions
    prep_time = models.IntegerField()  # Time in minutes
    cook_time = models.IntegerField()  # Time in minutes
    servings = models.IntegerField()
    image = models.ImageField(upload_to='recipes/images/', null=True, blank=True)  # Recipe image
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Link to Category
    collection = models.ManyToManyField(Collection, blank=True)  # Link to Collection (optional)
    recipe_type = models.CharField(max_length=10, choices=TITLE_CHOICES, default='veg')  # New field for recipe type

    def __str__(self):
        return self.title
