# Generated by Django 4.2.1 on 2023-05-16 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id_provincia', models.IntegerField(max_length=4, primary_key=True, serialize=False)),
                ('provincia', models.CharField(max_length=100)),
            ],
        ),
    ]
