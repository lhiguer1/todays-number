from rest_framework import routers
from .viewset import NumberViewset

router = routers.DefaultRouter()
router.register(r'numbers', NumberViewset, basename='number')

urlpatterns = router.urls
