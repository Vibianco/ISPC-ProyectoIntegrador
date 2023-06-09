# Generated by Django 4.2.1 on 2023-05-21 13:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_venta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='provincia',
            options={},
        ),
        migrations.AlterField(
            model_name='numeros_rifas',
            name='id_numero',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='provincia',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterModelTable(
            name='provincia',
            table=None,
        ),
    ]
