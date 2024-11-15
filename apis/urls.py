from django.urls import path
from .views import *

urlpatterns = [
    # Vacansies
    path('vakansies',VakansiListAPIView.as_view(),name='Vakansies'),
    path('vakansi/create',VakansiCreateAPIView.as_view(),name='Create-Vakansi'),
    path('vakansi/retrive/<int:pk>',VacanciRetriveView.as_view(),name='Retrive-Vakansi'),
    path('vakansi/update/<int:pk>',VacanciRetriveUpdateView.as_view(),name='Update-Vakansi'),
    path('vakansi/delete/<int:pk>',VacansiDestroyAPIView.as_view(),name='Delete-Vakansi'),
    # Requests 
    path('requests',RequestListAPIView.as_view(),name='Requests'),
    path('request/create',RequestCreateAPIView.as_view(),name='Create-Request'),
    path('request/retrive/<int:pk>',RequestRetriveView.as_view(),name='Retrive-Request'),
    path('request/delete/<int:pk>',RequestDestroyAPIView.as_view(),name='Delete-Request'),

]
