from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=400)
    date = models.DateField()
    address = models.CharField(max_length=100)