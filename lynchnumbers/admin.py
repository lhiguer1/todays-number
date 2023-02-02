from django.contrib import admin
from .models import Number

# Register your models here.
class NumberAdmin(admin.ModelAdmin):
    fields = [
        'date',
        'number',
        'url',
        'transcript',
    ]
    list_display = ['date', 'number', 'url']
    list_filter = ['date']

    def get_readonly_fields(self, request, obj=None):
        rofields = super().get_readonly_fields(request, obj)
        if obj:
            rofields += ('date',)
        return rofields




admin.site.register(Number, NumberAdmin)
