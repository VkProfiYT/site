from django.db import models

class Shop(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.PositiveIntegerField()
    salesAmount = models.PositiveIntegerField(default=0)
    isAvailable = models.BooleanField(default=True)
