# Generated by Django 4.1.4 on 2023-02-26 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_species_alter_animal_species'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='species',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.species'),
        ),
    ]
