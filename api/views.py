from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from db.models import Number
from django.core.cache import cache

# Create your views here.
def get_numbers(request: WSGIRequest, **kwargs):
    """Return a JsonResponse object of the dates and numbers of the specified dates."""
    year:int  = kwargs.get('year')
    month:int = kwargs.get('month')
    day:int   = kwargs.get('day')

    # cache_key is isoformat string; YYYY-MM-DD or YYYY-MM or YYYY
    cache_key = f'{year:04d}'
    if month:
        cache_key += f'-{month:02d}'
    if day:
        cache_key += f'-{day:02d}'

    if cached_data := cache.get(cache_key):
        json_numbers = cached_data

    else:
        numbers = Number.objects.filter(date__year=year)

        if month:
            numbers = numbers.filter(date__month=month)
        if day:
            numbers = numbers.filter(date__day=day)

        json_numbers = {number.date.isoformat(): number.number for number in numbers}

        cache.set(cache_key, json_numbers, None)

    return JsonResponse(json_numbers)
                        