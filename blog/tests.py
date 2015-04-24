from django.test import TestCase

from datetime import datetime
import re
from collections import Counter

from blog.models import *

def get_ingredients(ingredients):
    return Ingredient.objects.filter(name__in=ingredients)

class RecipeTests(TestCase):
    fixtures = ['recipes']

    def setUp(self):
        self.recipe = Recipe.objects.get(name='Big Boy Cake')

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


class RelatedPosts(TestCase):
    fixtures = ['recipes']

    def setUp(self):
        posts = [
            'Big Boy Cake',
            'Springtime Fresh Blueberry Pie',
            'Healthy Banana Pancakes'
        ]
        self.posts = Post.objects.filter(title__in=posts)

    def test_related_recipe(self):
        post = Post.objects.first()
        related = Post.objects.related(post)
        return self.assertEqual(Counter(related), Counter(self.posts))


class RecipeBrowserTests(TestCase):
    fixtures = ['recipes']

    def test_filter_one_ingredient(self):
        form = {
            'ingredients': get_ingredients(['flour'])
        }
        expected_names = [
            'Springtime Fresh Blueberry Pie',
            'Big Boy Cake'
        ]
        results = Recipe.browser.filter(form)

        self.assertEqual([r.name for r in results], expected_names)

    def test_filter_one_diet(self):
        form = {
            'diets': [Diet.objects.get(name='Vegetarian')]
        }
        expected_names = [
            'Springtime Fresh Blueberry Pie',
            'Healthy Banana Pancakes'
        ]
        results = Recipe.browser.filter(form)

        self.assertEqual([r.name for r in results], expected_names)

    def test_filter_one_meal_type(self):
        form = {
            'meal_type': MealType.objects.get(name='dinner')
        }
        expected_names = [
            'Taco Bowls',
            'Quinoa Taco Bake'
        ]
        results = Recipe.browser.filter(form)

        self.assertEqual([r.name for r in results], expected_names)

    def test_filter_one_ingredient_and_diet(self):
        form = {
            'ingredients': get_ingredients(['flour']),
            'diets': [Diet.objects.get(name='Vegetarian')]
        }
        expected_names = [
            'Springtime Fresh Blueberry Pie'
        ]
        results = Recipe.browser.filter(form)

        self.assertEqual([r.name for r in results], expected_names)

    def test_filter_two_ingredients(self):
        form = {
            'ingredients': get_ingredients(['flour', 'blueberries']),
        }
        expected_names = [
            'Springtime Fresh Blueberry Pie'
        ]
        results = Recipe.browser.filter(form)

        self.assertEqual([r.name for r in results], expected_names)



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