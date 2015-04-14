from django.test import TestCase

from blog.models import Recipe, Ingredient, MealType, Diet

def get_ingredients(ingredients):
    return [Ingredient.objects.get(name=n) for n in ingredients]

class RecipeTests(TestCase):
    fixtures = ['recipes']

    def setUp(self):
        self.recipe = Recipe.objects.get(name='Buttered Toast')

    def test_has_all_ingredients_true(self):
        ingredients = get_ingredients(['butter', 'bread'])

        self.assertTrue(self.recipe.has_all_ingredients(ingredients))

    def test_has_all_ingredients_empty(self):
        ingredients = []

        self.assertTrue(self.recipe.has_all_ingredients(ingredients))

    def test_total_time(self):
        total_time = self.recipe.prep_time + self.recipe.cook_time
        self.assertEqual(self.recipe.total_time(), total_time)


class RecipeBrowserTests(TestCase):
    fixtures = ['recipes']

    def test_recipe_browser_by_ingredient(self):
        ingredients = get_ingredients(['butter', 'bread'])
        matches = Recipe.browser.filter(ingredients=ingredients)
        for m in matches:
            for i in ingredients:
                self.assertTrue(i in m.ingredients.all())

    def test_all_ingredients_have_recipes(self):
        ingredients = Ingredient.browser.all()
        for i in ingredients:
            self.assertFalse(i.recipes.count() == 0)
