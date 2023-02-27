# Generated by Django 4.1.4 on 2023-02-26 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_animal_species'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='species',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.species'),
            preserve_default=False,
        ),
    ]
