from django.contrib import admin
from .models import Product, Recipe

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'category')

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('products',)