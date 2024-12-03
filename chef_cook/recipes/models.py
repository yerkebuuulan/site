from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    quantity = models.CharField(max_length=50, verbose_name="Количество")
    category = models.CharField(max_length=100, verbose_name="Категория")
    image = models.URLField(verbose_name="URL изображения")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"


class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название рецепта")
    steps = models.TextField(verbose_name="Шаги приготовления")
    products = models.ManyToManyField(Product, verbose_name="Продукты")

    image = models.URLField(verbose_name="URL изображения рецепта", blank=True, null=True)

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.title