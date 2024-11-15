from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveAPIView , RetrieveUpdateAPIView , DestroyAPIView

from .serializers import *
from .models import *

# Vacancy Part 
class VakansiListAPIView(ListAPIView):
    queryset = Vakansi.objects.all().order_by("-id")
    serializer_class = VakansiSerializer

class VakansiCreateAPIView(CreateAPIView):
    serializer_class = VakansiSerializer

class VacanciRetriveView(RetrieveAPIView):
    queryset = Vakansi.objects.all()
    serializer_class = VakansiSerializer

class VacanciRetriveUpdateView(RetrieveUpdateAPIView):
    queryset = Vakansi.objects.all()
    serializer_class = VakansiSerializer

class VacansiDestroyAPIView(DestroyAPIView):
    queryset = Vakansi.objects.all()
    serializer_class = Vakansi.objects.all()

# Request to Vacancy 
class RequestListAPIView(ListAPIView):
    queryset = Request.objects.all().order_by("-id")
    serializer_class = RequestSerializer

class RequestCreateAPIView(CreateAPIView):
    serializer_class = RequestSerializer

class RequestRetriveView(RetrieveAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class RequestDestroyAPIView(DestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = Request.objects.all()