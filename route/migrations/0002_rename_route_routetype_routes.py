# Generated by Django 4.2.5 on 2023-09-26 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='routetype',
            old_name='route',
            new_name='routes',
        ),
    ]
