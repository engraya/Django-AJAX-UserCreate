from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.name