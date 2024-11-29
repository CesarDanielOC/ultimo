# Generated by Django 5.1.2 on 2024-11-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id_pedido', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('id_cliente', models.IntegerField()),
                ('fecha_receta', models.CharField(max_length=100)),
                ('total_pedido', models.IntegerField()),
                ('estado_pedido', models.CharField(max_length=100)),
                ('metodo_pago', models.CharField(max_length=100)),
                ('direccion_envio', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]