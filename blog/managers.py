from django.db import models

class RecipeBrowserManager(models.Manager):
    def filter(self, **kwargs):
        ingredients = kwargs['ingredients']
        recipes = self.model.objects.all()
        return [r for r in recipes if r.has_all_ingredients(ingredients)]

