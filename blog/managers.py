from django.db import models
from django.db.models import Count

class RecipeBrowserManager(models.Manager):
    def filter(self, **kwargs):
        ingredients = kwargs.get('ingredients', [])
        recipes = self.all()
        return [r for r in recipes if
                r.has_all_ingredients(ingredients)]

    def all(self):
        return [r for r in self.model.objects.all()
                if r.has_post()]


class IngredientBrowserManager(models.Manager):
    def all(self):
        return self.model.objects.annotate(
            recipe_count=Count('recipes')).filter(recipe_count__gt=0)
