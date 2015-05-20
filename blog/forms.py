from django import forms

from haystack.forms import SearchForm

from blog.models import Recipe, Ingredient, MealType, Diet

def with_recipe_count(model):
        return [
                    (x, "{} ({})".format(x, x.recipes.count()))
                     for x in model.objects.all()
                     if x.recipes.count() > 0
        ]

class RecipeBrowserForm(forms.Form):

    def ingredients_list():
        return with_recipe_count(Ingredient)

    def meal_types_list():
        return with_recipe_count(MealType)

    def diets_list():
        return with_recipe_count(Diet)

    ingredients = forms.TypedMultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'browser-ingredients'}
        ),
        choices=ingredients_list,
        coerce=(lambda n: Ingredient.objects.get(name=n))
    )

    meal_type = forms.TypedChoiceField(
        required=False,
        widget=forms.RadioSelect(
            attrs={'class': 'browser-mealtypes'}
        ),
        choices=meal_types_list,
        coerce=(lambda n: MealType.objects.get(name=n))
    )

    diets = forms.TypedMultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'browser-diets'}
        ),
        choices=diets_list,
        coerce=(lambda n: Diet.objects.get(name=n))
    )