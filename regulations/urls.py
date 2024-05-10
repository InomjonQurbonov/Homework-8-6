from django.urls import path, include
from rest_framework import routers

from regulations.views import RegulationsViewSet

router = routers.DefaultRouter()

router.register(r'regulations', RegulationsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]