from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=25)
    message = models.CharField(max_length=225)