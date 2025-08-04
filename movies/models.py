from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    actors = models.ManyToManyField(Actor, related_name='movies')
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    rating = models.DecimalField(max_digits=3, decimal_places=1, help_text="Rating out of 10")

    def __str__(self):
        return self.title
