# recipes/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Book

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Поле для ввода email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Поля формы

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Сохраняем email
        if commit:
            user.save()  # Сохраняем пользователя
        return user

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'description', 'price']