from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib import admin
from ckeditor.fields import RichTextField
from djfractions.models import DecimalFractionField
import djfractions



class Recipe(models.Model):
	name = models.CharField(max_length=200, blank=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
	date =  models.DateTimeField(auto_now_add=True)
	headerimage = models.ImageField(null=True, blank=True, upload_to="images/")
	equipment = models.ManyToManyField("Equipment", blank=True)
	preptime = models.CharField(max_length=200, blank=True)
	cooktime = models.CharField(max_length=200, blank=True)
	portion = models.CharField(max_length=200, blank=True)
	# description = RichTextField(blank=True, null=True)
	intro = RichTextField(blank=True, null=True)
	course = models.ManyToManyField("Course", blank=True)
	cuisine = models.ManyToManyField("Cuisine", blank=True)
	source = models.CharField(max_length=200, blank=True)
	sourceurl = models.URLField(max_length=200, blank=True)
	notes = models.CharField(max_length=2000, blank=True, null=True)

	def __str__(self):
		return self.name


	def get_text(self):
		a = []
		for step in self.RecipeSteps.all():
			ingredients = []
			for ingredient in step.RecipeIngredients.all():
				ingredients.append((ingredient.ingredientname, ingredient.amount, ingredient.unit, ingredient.step))
			a.append((step.stepname, ingredients))
		
		return a

	def get_text_steps(self):
		b = []
		for step in self.RecipeSteps.all():
			b.append((step.stepname, step.steptext))

		return b

class Ingredient(models.Model):
	name = models.CharField(max_length=200, blank=True)
	fat = models.IntegerField(blank=True, null=True)
	saturatedfat = models.IntegerField(blank=True, null=True)
	sodium = models.IntegerField(blank=True, null=True)
	carbohydrates = models.IntegerField(blank=True, null=True)
	fiber = models.IntegerField(blank=True, null=True)
	sugar = models.IntegerField(blank=True, null=True)
	protein = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.name




class Equipment(models.Model):
	name = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.name

class Cuisine(models.Model):
	name = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.name

class Unit(models.Model):
	name = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.name


class RecipeStepManager(models.Manager):
    def all(self):
        return self.prefetch_related('RecipeIngredients', 'RecipeIngredients__unit', 'RecipeIngredients__ingredientname',)

class RecipeStep(models.Model):
		recipe = models.ForeignKey(Recipe, related_name='RecipeSteps', on_delete=models.CASCADE)
		stepname = models.CharField(max_length=200, blank=True, default="step one")
		steptext = RichTextField(blank=True, null=True)

		objects = RecipeStepManager()

		def __str__(self):
			return str(self.stepname)

class RecipeIngredient(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	ingredientname = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	amount = djfractions.models.DecimalFractionField(max_digits=5, decimal_places=5, blank=True, null=True)
	unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True)
	step = models.ForeignKey(RecipeStep, related_name='RecipeIngredients', on_delete=models.CASCADE, blank=True, null=True, default="1")

	def __str__(self):
		return str(self.ingredientname)