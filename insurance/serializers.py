from rest_framework.serializers import ModelSerializer
from .models import Policy

class PolicySerializers(ModelSerializer):
    class Meta:
        model= Policy
        fields="__all__"