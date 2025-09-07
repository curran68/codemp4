# bands/models.py

from django.db import models

class Band(models.Model):
    """
    A model to represent a musical band.
    """
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Concert(models.Model):
    """
    A model to represent a concert event.
    """
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
