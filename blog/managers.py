from django.db import models
from django.db.models import Count

class PostManager(models.Manager):

    def published(self):
        return self.get_queryset().filter(published=True)

    def food(self):
        return self.published().filter(type='FOOD')

    def fashion(self):
        return self.published().filter(type='FASHION')

    def travel(self):
        return self.published().filter(type='TRAVEL')

class RecipeBrowserManager(models.Manager):
    def filter(self, form):
        ingredients = form.get('ingredients', [])
        meal_type = form.get('meal_type', None)
        diets = form.get('diets', [])
        recipes = self.model.objects

        if meal_type:
            recipes = recipes.filter(meal_type__name=meal_type.name)

        for i in ingredients:
            recipes = recipes.filter(ingredients__name=i)

        for d in diets:
            recipes = recipes.filter(diets__name=d.name)

        return recipes