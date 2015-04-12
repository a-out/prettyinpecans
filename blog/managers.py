from django.db import models

class RecipeBrowserManager(models.Manager):
    def filter(self, **kwargs):
        ingredients = kwargs.get('ingredients', [])
        recipes = self.all()
        return [r for r in recipes if
                r.has_all_ingredients(ingredients)]

    def all(self):
        return [r for r in self.model.objects.all()
                if r.has_post()]