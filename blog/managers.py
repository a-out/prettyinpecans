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
    def filter(self, **kwargs):
        ingredients = kwargs.get('ingredients', [])
        recipes = self.all()
        return [r for r in recipes if
                r.has_all_ingredients(ingredients)]

    def all(self):
        return self.model.objects.all()


class IngredientBrowserManager(models.Manager):
    def all(self):
        return self.model.objects.annotate(
            recipe_count=Count('recipes')).filter(recipe_count__gt=0)
