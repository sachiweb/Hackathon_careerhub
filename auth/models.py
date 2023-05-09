from django.db import models
from django.contrib import admin
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    link=models.URLField(default=0)


    def __str__(self):
        return self.title