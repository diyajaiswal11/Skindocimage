from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ImageUploadSerializer
from .models import ImageUpload


class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset=ImageUpload.objects.all()
    serializer_class=ImageUploadSerializer