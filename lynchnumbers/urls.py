from django.urls import path
from .routers import TodaysNumberRouter
from .viewset import NumberViewset
from .views import StatisticsView


router = TodaysNumberRouter()
router.register(r'numbers', NumberViewset, basename='number')

urlpatterns = [
    path('statistics/', StatisticsView.as_view(), name='statistics'),
]

urlpatterns += router.urls
