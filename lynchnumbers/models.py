from django.db import models
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    RegexValidator,
)

class Number(models.Model):
    date = models.DateField(primary_key=True)
    number = models.PositiveSmallIntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(10)])

    yt_video_id = models.CharField(verbose_name='YouTube Video ID', blank=False, max_length=11, validators=[RegexValidator(regex=r'^[\w\-]{11}$')])
    yt_video_transcript = models.TextField(verbose_name='YouTube Video Transcript', blank=False)

    class Meta:
        ordering = ['date']
        get_latest_by = 'date'
    
    def __str__(self):
        return self.date.isoformat()

    @property
    def yt_video_url(self):
        return 'https://youtu.be/{}'.format(self.yt_video_id)
