from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from app_news.models import News, Announcement
from app_news.serializers import NewsSerializer, AnnouncementSerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
