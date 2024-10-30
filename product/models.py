from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=60)
    distant = models.IntegerField()
    description = models.CharField(max_length=120)
    image_relative_url = models.CharField(max_length=120, null=True, blank=True)