from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    publication = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(blank=True,null=True)
    text = models.TextField()

    def __str__(self):
        return self.title

class ArticleImage(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True)

class Event(models.Model):
    name = models.CharField(max_length=1000)
    organization = models.CharField(max_length=100,null=True)
    type = models.CharField(max_length=100,null=True)
    place = models.CharField(max_length=100,null=True)
    date = models.DateField(default=datetime.now,blank=True)
    image = models.ImageField(blank=True,null=True)
    phone_number = models.CharField(max_length=100,default="")
    text = models.TextField(default="")

    def __str__(self):
        return self.name

class EventImage(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True)