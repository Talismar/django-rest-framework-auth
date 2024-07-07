from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import ArticheModelSerializer
from core.models import Artiche


class ArticheModelViewSet(ModelViewSet):
    queryset = Artiche.objects.all()
    serializer_class = ArticheModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
