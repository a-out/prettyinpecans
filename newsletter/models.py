from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    joined = models.DateField(auto_now=True)

    def __str__(self):
        return self.email
