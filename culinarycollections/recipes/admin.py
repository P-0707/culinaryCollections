from django.contrib import admin
from .models import Recipe, Category, Collection
from ckeditor.widgets import CKEditorWidget
from django import forms

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'  # Include all fields in the form
        widgets = {
            'description': CKEditorWidget(),  # Use CKEditor for the description field
            'ingredients': CKEditorWidget(),   # Use CKEditor for the ingredients field
            'instructions': CKEditorWidget(),   # Use CKEditor for the instructions field
        }

class RecipeAdmin(admin.ModelAdmin):
    form = RecipeForm
    list_display = ('title', 'recipe_type', 'category')  # Display title, recipe_type, and category in the admin list view

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
admin.site.register(Collection)
