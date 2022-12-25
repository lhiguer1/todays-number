from django.urls import path
from .routers import TodaysNumberRouter
from .views import StatisticsView, NumberViewset


router = TodaysNumberRouter()
router.register(r'numbers', NumberViewset, basename='number')

urlpatterns = [
    path('statistics/', StatisticsView.as_view(), name='statistics'),
]

urlpatterns += router.urls
