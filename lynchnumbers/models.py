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
    yt_video = models.FileField("YouTube Video", upload_to='lynchvideos')

    class Meta:
        ordering = ['date']
        get_latest_by = 'date'
    
    def __str__(self):
        return self.date.isoformat()

    @property
    def yt_video_url(self):
        return 'https://youtu.be/{}'.format(self.yt_video_id)


class LynchVideo(models.Model):
    video = models.FileField(upload_to='lynchvideos')


class LynchVideoInfo(models.Model):
    videoId = models.CharField(null=True, blank=True, unique=True, max_length=11, validators=[RegexValidator(regex=r'^[\w\-]{11}$')])
    publishedAt = models.DateField(null=True, blank=True)
    transcript = models.TextField(null=True, blank=True)
    number = models.PositiveSmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    video = models.OneToOneField(LynchVideo, on_delete=models.CASCADE)

    class Meta:
        ordering = ['publishedAt']
        get_latest_by = 'publishedAt'

    @property
    def videoURL(self):
        return 'https://youtu.be/{}'.format(self.videoId)