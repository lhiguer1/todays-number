from rest_framework import routers
from .viewset import NumberViewset


# register_converter(FourDigitYearConverter, 'yyyy')
# register_converter(TwoDigitMonthConverter, 'mm')
# register_converter(TwoDigitDayConverter, 'dd')

# urlpatterns = [
#     path('', NumberListCreateAPIView.as_view(), name='number-list'),
#     path('<yyyy:year>/', NumberListAPIView.as_view(), name='number-year-list'),
#     path('<yyyy:year>/<mm:month>/', NumberListAPIView.as_view(), name='number-month-list'),
#     path('<yyyy:year>/<mm:month>/<dd:day>/', NumberRetrieveUpdateDestroyAPIView.as_view(), name='number-detail'),
# ]

router = routers.DefaultRouter()
router.register(r'numbers', NumberViewset, basename='number')

urlpatterns = router.urls
