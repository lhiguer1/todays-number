from datetime import date
from django.db import models

# Create your models here.
class Number(models.Model):
    date = models.DateField()
    number = models.PositiveSmallIntegerField(null=True, blank=True)
    url = models.URLField()
    transcript = models.TextField()

    class Meta:
        ordering = ['date']

    def today(self):
        self.filter(date=date.today())

    def __str__(self):
        return self.date.isoformat()

    def __eq__(self, other):
        return self.date == other.date

    def __nq__(self, other):
        return self.date != other.date

    def __lt__(self, other):
        return self.date < other.date

    def __le__(self, other):
        return self.date <= other.date

    def __gt__(self, other):
        return self.date > other.date

    def __ge__(self, other):
        return self.date >= other.date
