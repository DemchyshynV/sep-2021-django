# Generated by Django 4.0.3 on 2022-04-05 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_carmodel_auto_park'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carmodel',
            options={'ordering': ('id',), 'verbose_name': 'Car'},
        ),
    ]
