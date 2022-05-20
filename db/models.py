from datetime import date
from django.db import models

# Create your models here.
class Number(models.Model):
    date:date = models.DateField(primary_key=True)
    number:int = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['date']

    def today(self):
        self.filter(date=date.today())

    def to_json(self):
        return {self.date.isoformat(): self.number}

    def __str__(self):
        return f'{self.date.isoformat()} / {self.number:02}'

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
