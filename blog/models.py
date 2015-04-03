from django.db import models
from django.conf import settings

import markdown

def render_markdown(md_text, images):
    image_ref = ""

    for image in images:
        image_url = image.image.url
        image_ref = "{}\n[{}]: {}".format(image_ref, image, image_url)

    md = "{}\n{}".format(md_text, image_ref)
    return markdown.markdown(md)

class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images")

    def image_tag(self):
        return '<img src="{}" />'.format('/static/' + self.image.url)
    image_tag.allow_tags = True

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    written_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    body = models.TextField()
    images = models.ManyToManyField(Image)
    header_image = models.ForeignKey(Image, related_name='title_post')

    def html(self):
        return render_markdown(self.body, self.images.all())

    def pretty_date(self):
        day = self.written_on.strftime("%d").lstrip("0")
        month_name = self.written_on.strftime("%B")
        return "{} {}".format(month_name, day)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MealType(models.Model):
    name = models.CharField(max_length=32)

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
    name = models.CharField(max_length=2, choices=DIETS)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    SEASONS = (
        ('SP', 'Spring'),
        ('SU', 'Summer'),
        ('FA', 'Fall'),
        ('WI', 'Winter')
    )
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    diets = models.ManyToManyField(Diet)
    mealTypes = models.ManyToManyField(MealType)
    season = models.CharField(max_length=2, choices=SEASONS)
    calories = models.IntegerField()

    def __str__(self):
        return self.name