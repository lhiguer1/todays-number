from django.contrib import admin
from .models import Number

# Register your models here.
class NumberAdmin(admin.ModelAdmin):
    fields = [
        'date',
        'number',
        'yt_video_id',
        'yt_video_transcript',
    ]
    list_display = ['date', 'number', 'yt_video_url']
    list_filter = ['date']

    def get_readonly_fields(self, request, obj=None):
        rofields = super().get_readonly_fields(request, obj)
        if obj:
            rofields += ('date',)
        return rofields




admin.site.register(Number, NumberAdmin)
