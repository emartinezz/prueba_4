# Generated by Django 3.2.3 on 2021-07-01 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasteleria', '0002_remove_dato_contraseña'),
    ]

    operations = [
        migrations.AddField(
            model_name='dato',
            name='contraseña',
            field=models.CharField(default='', max_length=20),
        ),
    ]
