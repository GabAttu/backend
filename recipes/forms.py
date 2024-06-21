from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'prep_time', 'cook_time']


# recipes/forms.py

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('La password deve essere lunga almeno 8 caratteri.')
        if not re.search(r'\d', password):
            raise ValidationError('La password deve contenere almeno un numero.')
        if not re.search(r'[A-Z]', password):
            raise ValidationError('La password deve contenere almeno una lettera maiuscola.')
        if not re.search(r'[a-z]', password):
            raise ValidationError('La password deve contenere almeno una lettera minuscola.')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError('La password deve contenere almeno un carattere speciale.')
        return password

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user




class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

