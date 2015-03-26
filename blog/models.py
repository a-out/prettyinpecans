from django.db import models
from django.conf import settings

import markdown

def render_markdown(md_text, images):
    image_ref = ""

    for image in images:
        image_url = settings.STATIC_URL + image.image.url
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

    def html(self):
        return render_markdown(self.body, self.images.all())

    def __str__(self):
        return self.title
