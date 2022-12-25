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
    readonly_fields = ['date']

admin.site.register(Number, NumberAdmin)
