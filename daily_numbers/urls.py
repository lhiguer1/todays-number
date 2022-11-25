from django.urls import path, register_converter
from . import views, converters


register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.TwoDigitMonthConverter, 'mm')
register_converter(converters.TwoDigitDayConverter, 'dd')

urlpatterns = [
    path('', views.NumberListCreateAPIView.as_view(), name='number-list'),
    path('<yyyy:year>/', views.NumberListAPIView.as_view(), name='number-year-list'),
    path('<yyyy:year>/<mm:month>/', views.NumberListAPIView.as_view(), name='number-month-list'),
    path('<yyyy:year>/<mm:month>/<dd:day>/', views.NumberRetrieveUpdateDestroyAPIView.as_view(), name='number-detail'),
]
