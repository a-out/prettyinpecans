from django.db import models
from django.conf import settings

from .managers import PostManager, RecipeBrowserManager, IngredientBrowserManager

import markdown
import uuid
from datetime import datetime
import os

def render_markdown(md_text, images=[]):
    image_ref = ""

    for image in images:
        image_url = image.image.url
        image_ref = "{}\n[{}]: {}".format(image_ref, image, image_url)

    md = "{}\n{}".format(md_text, image_ref)
    return markdown.markdown(md)

def random_file_path(img_instance, filename):
    now = datetime.now()
    file_ext = filename.split('.')[-1]
    path =  "{y}/{m}/{n}.{e}".format(
        y=now.year,
        m=now.month,
        n=uuid.uuid4().hex,
        e=file_ext
    )
    return os.path.join('images', path)

# -------------------------------------------------------------------

class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=random_file_path)

    def image_tag(self):
        return '<img src="{}" />'.format('/static/' + self.image.url)
    image_tag.allow_tags = True

    def __str__(self):
        return self.name

class Post(models.Model):
    TYPES = (
        ('FOOD', 'Food'),
        ('FASHION', 'Fashion'),
        ('TRAVEL', 'Travel')
    )

    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    type = models.CharField(max_length=16, choices=TYPES)
    written_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    body = models.TextField()
    images = models.ManyToManyField(Image)
    header_image = models.ForeignKey(Image, related_name='title_post')

    objects = PostManager()

    def html(self):
        return render_markdown(self.body, self.images.all())

    def pretty_date(self):
        day = self.written_on.strftime("%d").lstrip("0")
        month_name = self.written_on.strftime("%B")
        return "{} {}".format(month_name, day)

    def is_modified(self):
        return (self.edited_on - self.written_on).seconds > 2

    def truncated_body(self):
        return render_markdown(''.join(self.body.split('\n')[:1]),
                               self.images.all())

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    objects = models.Manager()
    browser = IngredientBrowserManager()

    def save(self, *args, **kwargs):
        # ingredient names should be all lowercase
        self.name = self.name.lower()
        super(Ingredient, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class MealType(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Diet(models.Model):
    DIETS = (
        ('DF', 'Dairy Free'),
        ('GF', 'Gluten Free'),
        ('RW', 'Raw'),
        ('VG', 'Vegan'),
        ('VT', 'Vegetarian'),
        ('NO', 'None')
    )
    name = models.CharField(max_length=2, choices=DIETS, default='NO', unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    SEASONS = (
        ('SPR', 'Spring'),
        ('SUM', 'Summer'),
        ('FAL', 'Fall'),
        ('WIN', 'Winter'),
        ('ANY', 'Any')
    )
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='recipes')
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    ingredients_text = models.TextField()
    description = models.TextField()
    instructions = models.TextField()
    diets = models.ManyToManyField(Diet)
    meal_type = models.ForeignKey(MealType, related_name='recipes')
    season = models.CharField(max_length=3, choices=SEASONS, default='ANY')
    calories = models.IntegerField()
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()

    objects = models.Manager()
    browser = RecipeBrowserManager()

    def ingredients_html(self):
        return render_markdown(self.ingredients_text)

    def instructions_html(self):
        return render_markdown(self.instructions)

    def total_time(self):
        return self.prep_time + self.cook_time

    def has_all_ingredients(self, ingredients):
        in_common = set(self.ingredients.all()).intersection(ingredients)
        return len(in_common) == len(ingredients)

    def image(self):
        return self.posts.first().header_image.image

    def __str__(self):
        return self.name
