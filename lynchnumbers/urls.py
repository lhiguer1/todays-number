from django.urls import path, include
from rest_framework import routers
from .views import StatisticsView, NumberViewset, HomeView, AboutView, DocumentationView


router = routers.DefaultRouter()
router.include_root_view = False

router.register(r'numbers', NumberViewset, basename='number')

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('docs/', DocumentationView.as_view(), name='docs'),
    path('api/', include(router.urls)),
    path('api/statistics/', StatisticsView.as_view(), name='statistics'),
]
