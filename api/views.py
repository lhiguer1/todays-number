from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from db.models import Number
from django.core.cache import cache

# Create your views here.
def make_key(year=None, month=None, day=None):
    # key is isoformat string; YYYY-MM-DD or YYYY-MM or YYYY
    key = f'{year:04d}'
    if month is not None:
        key += f'-{month:02d}'
    if day is not None:
        key += f'-{day:02d}'

    return key

def get_numbers(request: WSGIRequest, **kwargs):
    """Return a JsonResponse object of the dates and numbers of the specified dates."""
    year:int  = kwargs.get('year')
    month:int = kwargs.get('month')
    day:int   = kwargs.get('day')

    # TODO: come back to cache
    numbers = Number.objects.filter(date__year=year)
    if month:
        numbers = numbers.filter(date__month=month)
    if day:
        numbers = numbers.filter(date__day=day)
    
    values = list(numbers.values('date', 'number', 'urlid', 'transcript'))

    return JsonResponse({'numbers': values}, status=200)
                        