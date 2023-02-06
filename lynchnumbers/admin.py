from django.contrib import admin
from .models import Number, LynchVideo, LynchVideoInfo

# Register your models here.
class NumberAdmin(admin.ModelAdmin):
    fields = [
        'date',
        'number',
        'yt_video_id',
        'yt_video_transcript',
        'yt_video',
    ]
    list_display = ['date', 'number', 'yt_video_url']
    list_filter = ['date']

    def get_readonly_fields(self, request, obj=None):
        rofields = super().get_readonly_fields(request, obj)
        if obj:
            rofields += ('date',)
        return rofields


class LynchVideoAdmin(admin.ModelAdmin):
    fields = [
        'video',
    ]


class LynchVideoInfoAdmin(admin.ModelAdmin):
    fields = [
        'videoId',
        'publishedAt',
        'transcript',
        'number',
        'lynchVideoId',
    ]

admin.site.register(Number, NumberAdmin)
admin.site.register(LynchVideo, LynchVideoAdmin)
admin.site.register(LynchVideoInfo, LynchVideoInfoAdmin)
