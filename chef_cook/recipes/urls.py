from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import create_book, book_list, edit_book, delete_book

urlpatterns = [
    path('', views.index, name='index'),
    path('sclad/', views.sclad, name='sclad'),
    path('contacts/', views.contacts, name='contacts'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='recipes/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('books/', views.book_list, name='book_list'),
    path('add/', views.create_book, name='create_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
]