from django.urls import path
from rest_framework import routers
from .views import StatisticsView, NumberViewset


router = routers.DefaultRouter()
router.include_root_view = False

router.register(r'numbers', NumberViewset, basename='number')

urlpatterns = router.urls + [
    path('statistics/', StatisticsView.as_view(), name='statistics'),
]
