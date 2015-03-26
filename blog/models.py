from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    written_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    body = models.TextField()

    def __str__(self):
        return self.title
