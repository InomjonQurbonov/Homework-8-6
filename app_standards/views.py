from django.shortcuts import render
from rest_framework import viewsets

from app_standards.models import Standards
from app_standards.serializers import StandardsSerializer, GetStandardsSerializer
from app_standards.permissions import IsAdminOrReadOnly


class StandardsViewSet(viewsets.ModelViewSet):
    queryset = Standards.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetStandardsSerializer
        return StandardsSerializer
