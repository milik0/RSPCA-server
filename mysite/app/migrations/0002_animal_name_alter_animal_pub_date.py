# Generated by Django 4.1.4 on 2023-02-26 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='name',
            field=models.CharField(default='none', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='animal',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]