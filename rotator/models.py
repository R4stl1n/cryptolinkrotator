from django.db import models
from django.utils import timezone

class Rotator(models.Model):
    rotator_name = models.CharField(max_length=200)
    rotator_owner = models.CharField(max_length=200)
    rotator_slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    current_index = models.IntegerField(default=0)

    def __str__(self):
        return self.rotator_name + ' - Rotator'

class RotatorLink(models.Model):
    rotator = models.ForeignKey(Rotator, on_delete=models.CASCADE)
    rotator_link = models.CharField(max_length=200,unique=True)
    discord_user_name = models.CharField(max_length=200)
    times_viewed = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rotator.rotator_name + ' - ' +self.discord_user_name + ' - Rotator Link'