from django.db import models


NATIONATIONALITY_CHOICES = (
    ('American', 'American'),
    ('British', 'British'),
    ('Canadian', 'Canadian'),
    ('Australian', 'Australian'),
    ('Indian', 'Indian'),
    ('Other', 'Other'),
)


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=50, choices=NATIONATIONALITY_CHOICES, default='Other')

    def __str__(self):
        return self.name
