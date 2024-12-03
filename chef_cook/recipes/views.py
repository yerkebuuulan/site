# recipes/views.py
from django.shortcuts import render, redirect
from .models import Product, Recipe
from .forms import UserRegistrationForm
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Book
from .forms import BookForm

def index(request):
    recipes = Recipe.objects.all()[:3]  # Показываем 3 последних рецепта на главной
    user_name = request.user.username if request.user.is_authenticated else None
    return render(request, 'recipes/index.html', {'recipes': recipes, 'user_name': user_name})


def sclad(request):
    products = Product.objects.all().order_by('category')
    categories = Product.objects.values_list('category', flat=True).distinct()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'recipes/sclad.html', context)

def contacts (request):
    return render(request, 'recipes/contacts.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем пользователя
            return redirect('index')  # Перенаправляем на главную страницу
    else:
        form = UserRegistrationForm()
    return render(request, 'recipes/register.html', {'form': form})


def custom_logout(request):
    logout(request)  # Выход пользователя
    return redirect('index')  # Перенаправление на главную страницу

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'recipes/book_form.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'recipes/book_list.html', {'books': books})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'recipes/book_form.html', {'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'recipes/confirm_delete.html', {'book': book})