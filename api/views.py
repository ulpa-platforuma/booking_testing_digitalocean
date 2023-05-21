from django.shortcuts import render
from django.http import HttpResponse

from .models import Test
from .serializers import TestSerializer

from rest_framework import viewsets

# Create your views here.

class TestViewSet(viewsets.ModelViewSet):
    queryset=Test.objects.all()
    serializer_class=TestSerializer
