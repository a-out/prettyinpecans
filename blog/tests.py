from django.test import TestCase

from datetime import datetime
import re

from blog.models import *

def get_ingredients(ingredients):
    return Ingredient.objects.filter(name__in=ingredients)

class RecipeTests(TestCase):
    fixtures = ['recipes']

    def setUp(self):
        self.recipe = Recipe.objects.get(name='Big Boy Cake')

    def test_has_all_ingredients_true(self):
        ingredients = get_ingredients(['butter', 'flour'])

        self.assertTrue(self.recipe.has_all_ingredients(ingredients))

    def test_has_all_ingredients_empty(self):
        ingredients = []

        self.assertTrue(self.recipe.has_all_ingredients(ingredients))

    def test_total_time(self):
        total_time = self.recipe.prep_time + self.recipe.cook_time
        self.assertEqual(self.recipe.total_time(), total_time)


class PostTests(TestCase):
    fixtures = ['posts']

    def setUp(self):
        self.post = Post.objects.get(title='Big Boy Cake')

    def test_published_only_returns_published_posts(self):
        posts = Post.objects.published()

        for p in posts:
            self.assertTrue(p.published)

    def test_post_has_recipes(self):
        self.assertTrue(self.post.recipes.count() > 0)


class RecipeBrowserTests(TestCase):
    fixtures = ['recipes']



class ImageTests(TestCase):
    fixtures = ['posts']

    def test_random_file_path_provides_correct_path(self):
        image = Image.objects.first()
        filename = 'test.jpg'
        year, month = datetime.now().year, datetime.now().month
        path = random_file_path(image, filename)
        image_dir = 'images/{}/{}/'.format(year, month)
        self.assertTrue(image_dir in path)
        self.assertTrue('jpg' in path)