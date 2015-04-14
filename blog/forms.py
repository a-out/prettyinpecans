from django import forms

from blog.models import Recipe, Ingredient

class RecipeBrowserForm(forms.Form):
    ingredients_list = [(i, "{} ({})".format(i.name, i.recipes.count()))
                        for i in Ingredient.browser.all()]

    ingredients = forms.TypedMultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'browser-ingredients'}
        ),
        choices=ingredients_list,
        coerce=(lambda n: Ingredient.objects.get(name=n))
    )
