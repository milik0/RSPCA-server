# Generated by Django 4.1.4 on 2023-02-26 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_animal_species'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='species',
        ),
        migrations.DeleteModel(
            name='Species',
        ),
    ]
