from rest_framework.serializers import ModelSerializer

from core.models import Artiche


class ArticheModelSerializer(ModelSerializer):
    class Meta:
        model = Artiche
        fields = ("id", "title", "content")
