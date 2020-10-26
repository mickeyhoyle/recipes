# Generated by Django 3.1.2 on 2020-10-26 14:19

from django.db import migrations
import djfractions.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0002_auto_20201026_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount',
            field=djfractions.models.fields.DecimalFractionField(blank=True, coerce_thirds=True, decimal_places=10, limit_denominator=None, max_digits=10, null=True),
        ),
    ]
