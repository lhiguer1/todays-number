from django.urls import path, register_converter
from .converters import FourDigitYearConverter, TwoDigitMonthConverter, TwoDigitDayConverter
from .views import NumberListAPIView, NumberListCreateAPIView, NumberRetrieveUpdateDestroyAPIView



register_converter(FourDigitYearConverter, 'yyyy')
register_converter(TwoDigitMonthConverter, 'mm')
register_converter(TwoDigitDayConverter, 'dd')

urlpatterns = [
    path('', NumberListCreateAPIView.as_view(), name='number-list'),
    path('<yyyy:year>/', NumberListAPIView.as_view(), name='number-year-list'),
    path('<yyyy:year>/<mm:month>/', NumberListAPIView.as_view(), name='number-month-list'),
    path('<yyyy:year>/<mm:month>/<dd:day>/', NumberRetrieveUpdateDestroyAPIView.as_view(), name='number-detail'),
]
