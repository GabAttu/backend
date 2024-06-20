from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_by = models.ManyToManyField(User, related_name='liked_recipes', blank=True)

def __str__(self):
        return self.title

