from django import template
from random import randrange, choice

register = template.Library()

ADJECTIVES = (
    "fluffy",
    "cheesy",
    "flaky",
    "irresistable",
    "palatable",
    "life-affirming",
    "natural",
    "gluteny",
    "juicy",
    "hearty",
    "crispy",
    "baked",
    "nutty",
    "wine-braised",
    "spice-rubbed"
)

FOOD_NOUNS = (
    "meat",
    "cheese",
    "pistachio",
    "almond",
    "kangaroo",
    "orange-peel",
    "kale",
    "lard",
    "fish",
    "seaweed",
    "polenta",
    "watermelon"
)

FORM_NOUNS = (
    "nuggets",
    "casserole",
    "clambake",
    "cupcakes",
    "tacos",
    "bowl",
    "dumplings",
    "buckets",
    "rations",
    "foie gras",
    "calamari",
    "sandwiches",
    "tenderloins",
    "rectangles",
    "wraps",
    "stew",
    "roast",
    "chili",
    "stir-fry",
    "dip"
)

def get_word(word_list, capitalize=False):
    return choice(word_list).capitalize() if capitalize else choice(word_list)

@register.simple_tag
def random_recipe_name():
    compound_name = randrange(4) == 0

    if compound_name:
        return "{} {} and {} {} {}".format(
            get_word(ADJECTIVES, True), get_word(FOOD_NOUNS), get_word(ADJECTIVES),
            get_word(FOOD_NOUNS), get_word(FORM_NOUNS)
        )
    else:
        return "{} {} {}".format(get_word(ADJECTIVES, True),
            get_word(FOOD_NOUNS), get_word(FORM_NOUNS))