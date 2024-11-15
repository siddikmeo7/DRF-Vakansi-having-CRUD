from rest_framework.serializers import ModelSerializer
from .models import *


class VakansiSerializer(ModelSerializer):
    class Meta:
        model = Vakansi
        fields = "__all__"

class RequestSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"


