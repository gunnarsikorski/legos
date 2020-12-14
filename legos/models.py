from django.db import models
from django.contrib.postgres.fields import ArrayField

class Lego(models.Model):
    name = models.CharField(max_length=200)
    set_number = models.PositiveIntegerField()
    piece_count = models.PositiveSmallIntegerField()
    source = models.CharField(max_length=200)
    release_year = models.PositiveSmallIntegerField()
    image_url = models.TextField(max_length=500, default=None)
    minifigures = ArrayField(models.CharField(max_length=50))
    set_series = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Review(models.Model):
    lego = models.ForeignKey(
        Lego, on_delete=models.CASCADE, related_name='reviews'
    )
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=800)

    def __str__(self):
        return self.title
