# Generated by Django 3.1.2 on 2020-10-27 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0005_auto_20201026_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
