from django.urls import path, include
from rest_framework import routers

from app_news.views import NewsViewSet, AnnouncementViewSet

router = routers.DefaultRouter()

router.register('news', NewsViewSet)
router.register('announcements', AnnouncementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]