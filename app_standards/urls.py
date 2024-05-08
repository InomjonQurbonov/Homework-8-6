from django.urls import path, include
from rest_framework import routers

from app_standards.views import StandardsViewSet

router = routers.DefaultRouter()

router.register(r'standards', StandardsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]