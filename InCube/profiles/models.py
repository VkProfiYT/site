from django.db import models

class Users(models.Model):
    discordId = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=16)
    description = models.TextField()
    roleId = models.IntegerField(default=1)
    avatar = models.ImageField(upload_to="avatar/", blank=True)
    links = models.JSONField(null=True, blank=True)
    socialCredits = models.IntegerField(default=0)

class Players(Users):
    bio = models.TextField()
    chanels = models.JSONField(null=True, default=dict)

class Roles(models.Model):
    title =  models.CharField(max_length=32)
    maxBio = models.IntegerField(default=512)
    isAvatarAvailable = models.BooleanField(default=False)
    canAddLinks = models.BooleanField(default=False)
    canPublishContent = models.BooleanField(default=False)
    canEditContent = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)
