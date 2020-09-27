from django.urls import path, include
from .views import *
from rest_framework import routers
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ImageUploadView
from django.views.decorators.csrf import csrf_exempt


# routers = routers.DefaultRouter()
# routers.register('',ImageUploadViewSet)

urlpatterns = [
   url(r'', csrf_exempt(ImageUploadView.as_view())),
]