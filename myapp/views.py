from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Canil
from .serializers import CanilSerializer

# Create your views here.
class CanilList(generics.ListCreateAPIView):

    queryset = Canil.objects.all()
    serializer_class = CanilSerializer

class CanilDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Canil.objects.all()
    serializer_class = CanilSerializer