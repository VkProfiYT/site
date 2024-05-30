from datetime import date
from typing import Any
from django.db import models
from django.urls import reverse
from .temple import *

class contents(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    authorId  = models.IntegerField()
    urlContent = models.CharField(max_length=64)
    datePublished = models.DateTimeField('date published', default=date.today)
    type = models.CharField(max_length=16)
    platformType = models.CharField(max_length=16)
    categories = models.CharField(max_length=16)
    rating = models.IntegerField()
    isMember = models.BooleanField()
    
    def __str__(self):
        return self.title + ": "+ self.urlContent
    
    def get_absolute_url(self):
        return reverse("content", kwargs={"id": self.pk})
    

