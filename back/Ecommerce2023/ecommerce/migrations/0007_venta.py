# Generated by Django 4.2.1 on 2023-05-18 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_numeros_rifas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('descuento', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('id_factura', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.factura')),
                ('id_rifa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.rifa')),
            ],
        ),
    ]