from django.urls import path, include
from rest_framework import routers

from app_dictionary.views import DictionaryViewSet

router = routers.DefaultRouter()

router.register('dictionary', DictionaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
