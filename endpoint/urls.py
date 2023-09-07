from django.urls import path
from .views import info_endpoint

urlpatterns = [
    path('',  info_endpoint,  name='info_endpoint'),
]
