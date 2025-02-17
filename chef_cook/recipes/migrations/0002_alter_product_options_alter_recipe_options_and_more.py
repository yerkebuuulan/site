# Generated by Django 5.1.2 on 2024-10-22 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category', 'name'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cooking_time',
            field=models.IntegerField(default=30, verbose_name='Время приготовления (минуты)'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(choices=[('easy', 'Легкий'), ('medium', 'Средний'), ('hard', 'Сложный')], default='medium', max_length=20, verbose_name='Сложность'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.URLField(blank=True, null=True, verbose_name='URL изображения рецепта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.URLField(verbose_name='URL изображения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.CharField(max_length=50, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(to='recipes.product', verbose_name='Продукты'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='steps',
            field=models.TextField(verbose_name='Шаги приготовления'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название рецепта'),
        ),
    ]
