# Generated by Django 4.2.1 on 2023-05-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_alter_usuario_id_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rifa',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
