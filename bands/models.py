# bands/models.py

from django.db import models
from django.utils.text import slugify

class Band(models.Model):
    """
    A model to represent a musical band.
    """
    name = models.CharField(max_length=100, unique=True)
    genre = models.CharField(max_length=50)
    # Add the slug field for unique URLs
    slug = models.SlugField(unique=True, blank=True)
    # Add other fields like bio, image, and logo as needed
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='bands/', blank=True, null=True)
    logo = models.ImageField(upload_to='bands/logos/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Automatically generate a slug from the name if it's not set
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

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