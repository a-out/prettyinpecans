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
        recipes = self.model.objects

        if meal_type:
            recipes = recipes.filter(meal_type__name=meal_type.name)

        return [r for r in recipes.all() if
                r.has_all_ingredients(ingredients)]