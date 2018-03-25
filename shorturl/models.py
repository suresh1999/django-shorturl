from django.db import models


# Create your models here.
class ShortUrl(models.Model):
    long_url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=20)

    def __str__(self):
        return self.short_url
