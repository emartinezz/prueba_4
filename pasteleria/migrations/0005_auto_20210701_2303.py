# Generated by Django 3.2.3 on 2021-07-02 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasteleria', '0004_remove_producto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='Cantidad_de_Personas',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='producto',
            name='Cantidad_de_Tortas',
            field=models.IntegerField(default=0),
        ),
    ]