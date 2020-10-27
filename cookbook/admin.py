from django.contrib import admin
from django.db import models
from .models import *
from django.forms import SelectMultiple
from django.contrib.admin.widgets import AutocompleteSelect
import djfractions

class RecipeIngredientInline(admin.TabularInline):
	autocomplete_fields = ['ingredientname', 'unit']
	model = RecipeIngredient
	extra = 0	



	def get_filters(self, obj):
		return (('stepname', dict(recipe=obj),),)

	def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
		"""
		Only allow choosing directions from the directions that are in this recipe
		"""
		field = super(RecipeIngredientInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

		if db_field.name == 'step':
		    if request._obj_:
		        field.queryset = field.queryset.filter(recipe=request._obj_)  
		    else:
		        field.queryset = field.queryset.none()

		return field
	
class RecipeStepInline(admin.TabularInline):
	model = RecipeStep
	extra = 0	

class IngredientAdmin(admin.ModelAdmin):
	ordering = ['id']
	search_fields = ['name']

class UnitAdmin(admin.ModelAdmin):
	search_fields = ['name']


class RecipeAdmin(admin.ModelAdmin):
	inlines = [RecipeStepInline, RecipeIngredientInline]
	fields = (
        'name', 
        'headerimage',
        ('source',
     	'sourceurl'),
		('preptime', 
		'cooktime'),
		'portion',
        ('equipment', 'course', 'cuisine'),
        'intro',
        'notes',
    )

	def save_model(self, request, obj, form, change):
		obj.author = request.user
		super().save_model(request, obj, form, change)

	def get_form(self, request, obj=None, **kwargs):

		request._obj_ = obj
		return super(RecipeAdmin, self).get_form(request, obj, **kwargs)

	


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient)
admin.site.register(Equipment)
admin.site.register(Course)
admin.site.register(Cuisine)
admin.site.register(Unit, UnitAdmin)
admin.site.register(RecipeStep) 


