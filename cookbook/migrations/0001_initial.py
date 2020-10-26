# Generated by Django 3.1.2 on 2020-10-24 11:26

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('fat', models.IntegerField(blank=True, null=True)),
                ('saturatedfat', models.IntegerField(blank=True, null=True)),
                ('sodium', models.IntegerField(blank=True, null=True)),
                ('carbohydrates', models.IntegerField(blank=True, null=True)),
                ('fiber', models.IntegerField(blank=True, null=True)),
                ('sugar', models.IntegerField(blank=True, null=True)),
                ('protein', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('headerimage', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('preptime', models.CharField(blank=True, max_length=200)),
                ('cooktime', models.CharField(blank=True, max_length=200)),
                ('portion', models.CharField(blank=True, max_length=200)),
                ('intro', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=200)),
                ('sourceurl', models.URLField(blank=True)),
                ('notes', models.CharField(blank=True, max_length=2000, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course', models.ManyToManyField(blank=True, to='cookbook.Course')),
                ('cuisine', models.ManyToManyField(blank=True, to='cookbook.Cuisine')),
                ('equipment', models.ManyToManyField(blank=True, to='cookbook.Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stepname', models.CharField(blank=True, default='step one', max_length=200)),
                ('steptext', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RecipeSteps', to='cookbook.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('ingredientname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.recipe')),
                ('step', models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RecipeIngredients', to='cookbook.recipestep')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cookbook.unit')),
            ],
        ),
    ]