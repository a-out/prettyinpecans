from django.db import models
from django.conf import settings

from .managers import PostManager, RecipeBrowserManager
from .utils import render_markdown, random_file_path, before_jump, teaser

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

    def get_absolute_url(self):
        return "/posts/{}".format(self.slug)

    def html(self):
        return render_markdown(self.body, self.images.all())

    def pretty_date(self):
        # remove leading 0 from day
        day = self.written_on.strftime("%d").lstrip("0")
        month_name = self.written_on.strftime("%B")
        year = self.written_on.strftime("%Y")
        return "{} {}, {}".format(month_name, day, year)

    def is_modified(self):
        return (self.edited_on - self.written_on).seconds > 2

    def truncated_html(self):
        return render_markdown(before_jump(self.body), self.images.all())

    def teaser(self):
        return render_markdown(teaser(self.body, 50))

    def recipes_list(self):
        if self.recipes.count() > 0:
            return ", ".join([r.name for r in self.recipes.all()])
        return ""

    def ingredients_list(self):
        if self.recipes.count() > 0:
            return ", ".join([r.ingredients_list() for r in self.recipes.all()])
        return ""

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

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
    name = models.CharField(max_length=32, unique=True)

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
    diets = models.ManyToManyField(Diet, related_name='recipes', blank=True)
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

    def image(self):
        return self.post.header_image.image

    def ingredients_list(self):
        return ", ".join([i.name for i in self.ingredients.all()])

    def __str__(self):
        return self.name
