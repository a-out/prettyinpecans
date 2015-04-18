from django import forms

from blog.models import Recipe, Ingredient, MealType

class RecipeBrowserForm(forms.Form):
    def objects_with_recipe_count(model):
        return [
                    (x, "{} ({})".format(x, x.recipes.count()))
                     for x in model.objects.all()
                     if x.recipes.count() > 0
        ]

    ingredients_list = objects_with_recipe_count(Ingredient)
    meal_types_list = objects_with_recipe_count(MealType)

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