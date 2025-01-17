# Generated by Django 5.1.2 on 2024-11-22 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id_promocion', models.PositiveSmallIntegerField(max_length=6, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_inicio', models.CharField(max_length=100)),
                ('fecha_fin', models.CharField(max_length=100)),
                ('descuento', models.PositiveSmallIntegerField()),
                ('productos_aplicados', models.CharField(max_length=100)),
                ('condiciones', models.CharField(max_length=100)),
            ],
        ),
    ]
