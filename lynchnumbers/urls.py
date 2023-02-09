from django.urls import path, include
from rest_framework import routers
from .views import (
    StatisticsView,
    NumberViewset,
    LynchVideoViewSet,
    LynchVideoInfoViewSet,
    HomeView,
    AboutView,
    DocumentationView,
)


router = routers.DefaultRouter()

router.register(r'numbers', NumberViewset, basename='number')
router.register(r'lynchvideos', LynchVideoViewSet)
router.register(r'lynchvideoinfo', LynchVideoInfoViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('docs/', DocumentationView.as_view(), name='docs'),
    path('api/', include(router.urls)),
    path('api/statistics/', StatisticsView.as_view(), name='statistics'),
]
