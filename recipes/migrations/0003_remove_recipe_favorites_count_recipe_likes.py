# Generated by Django 5.0.6 on 2024-06-18 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='favorites_count',
        ),
        migrations.AddField(
            model_name='recipe',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
