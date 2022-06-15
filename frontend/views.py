from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.
def home(request: WSGIRequest):
    return HttpResponse("<p>Today's Number<p>", status=200)
