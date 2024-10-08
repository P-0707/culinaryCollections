# Generated by Django 4.2.16 on 2024-10-06 15:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_type',
            field=models.CharField(choices=[('veg', 'Vegetarian'), ('non_veg', 'Non-Vegetarian'), ('vegan', 'Vegan')], default='veg', max_length=10),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
