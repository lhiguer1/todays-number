from django.contrib import admin
from .models import Number

# Register your models here.
class NumberAdmin(admin.ModelAdmin):
    list_display = ['date', 'number', 'url']
    list_filter = ['date']

admin.site.register(Number, NumberAdmin)
