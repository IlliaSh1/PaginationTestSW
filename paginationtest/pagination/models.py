from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    pages = models.IntegerField()
    somethings = models.CharField(max_length=20,default='a')

class Book_meta(models.Model):
    name = models.CharField(max_length=100)
    pages = models.IntegerField()
    desc = models.CharField(max_length=20)