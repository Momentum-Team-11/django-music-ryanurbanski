from django.db import models

class Albums(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)