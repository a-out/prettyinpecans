from django.test import TestCase

from blog.models import Post, Recipe, Ingredient, MealType, Diet

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

    def test_default_manager_returns_only_published(self):
        # todo: recreate this test
        pass

    def test_post_has_recipes(self):
        self.assertTrue(self.post.recipes.count() > 0)


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
