# Generated by Django 5.1.2 on 2024-11-26 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.CharField(max_length=100),
        ),
    ]
