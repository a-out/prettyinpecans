from django.db import models
from django.db.models import Count

from collections import Counter
from itertools import chain

class PostManager(models.Manager):
    RELATED_POST_COUNT = 3

    def published(self):
        return self.get_queryset().filter(published=True)

    def food(self):
        return self.published().filter(type='FOOD')

    def fashion(self):
        return self.published().filter(type='FASHION')

    def travel(self):
        return self.published().filter(type='TRAVEL')

    def related(self, post):
        if post.type == 'FOOD':
            return self._related_food(post.recipes.first())
        elif post.type == 'FASHION':
            return self.fashion()[:self.RELATED_POST_COUNT]
        else:
            return self.travel()[:self.RELATED_POST_COUNT]

    # find similar food posts based on recipe
    def _related_food(self, recipe):
        # for each ingredient of our recipe, find other recipes
        # that share the same ingredient. We'll end up with a 
        # flat list of recipes, with possible (probable) duplicates.
        similar_recipes = []
        for i in recipe.ingredients.all():
            similar_recipes += filter(
                lambda r: r.name != recipe.name, i.recipes.all())

        # get post of most similar recipes, according to the Counter
        most_similar = [r[0].post for r in 
            Counter(similar_recipes).most_common(self.RELATED_POST_COUNT)]

        # if not enough similar recipes were found, supplement with
        # some random food posts.
        if (len(most_similar) < self.RELATED_POST_COUNT):
            needed_posts = self.RELATED_POST_COUNT - len(most_similar)
            most_similar += self.food()[:needed_posts]

        return most_similar


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