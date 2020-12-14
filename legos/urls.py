from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, LegoViewSet

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'legos', LegoViewSet, basename='lego')
urlpatterns = router.urls