from django.urls import path, include
from rest_framework import routers

from app_leadership.views import LeadershipViewSet, DepartmentViewSet

router = routers.DefaultRouter()

router.register(r'department', DepartmentViewSet)
router.register(r'leadership', LeadershipViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
