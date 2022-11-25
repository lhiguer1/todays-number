from django.db import models
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    URLValidator,
)

class Number(models.Model):
    date = models.DateField(unique=True)
    number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    url = models.URLField(blank=False, validators=[URLValidator])
    transcript = models.TextField(blank=False)

    class Meta:
        ordering = ['date']
