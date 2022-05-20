from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from db.models import Number

# Create your views here.
def get_numbers(request: WSGIRequest, **kwargs):
    """Return a JsonResponse object of the dates and numbers of the specified dates."""

    numbers = Number.objects.filter(date__year=kwargs['year'])

    if month := kwargs.get('month'):
        numbers = numbers.filter(date__month=month)
    if day := kwargs.get('day'):
        numbers = numbers.filter(date__day=day)

    json_numbers = {number.date.isoformat(): number.number for number in numbers}
    return JsonResponse(json_numbers)
                        