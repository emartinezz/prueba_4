# Generated by Django 3.2.3 on 2021-07-03 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pasteleria', '0005_auto_20210701_2303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dato',
            options={'permissions': (('usuario', 'es usuario'),)},
        ),
    ]
