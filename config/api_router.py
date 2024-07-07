from rest_framework.routers import DefaultRouter

from core.api.viewsets import ArticheModelViewSet

router = DefaultRouter()

router.register(r"artiche", ArticheModelViewSet)

urlpatterns = router.urls
