from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app_news.models import News, Announcement
from app_news.serializers import NewsSerializer, AnnouncementSerializer


class CreateAuthorisedObject(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.path.startswith('/news/'):
            return NewsSerializer
        elif self.request.path.startswith('/announcements/'):
            return AnnouncementSerializer
        else:
            raise Exception('Invalid endpoint')

    def post(self, request):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(news_author=self.request.user)
        return Response(serializer.data, status=201)


class NewsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        serializer.save(news_author=self.request.user)


class AnnouncementViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def perform_create(self, serializer):
        serializer.save(anno_author=self.request.user)

