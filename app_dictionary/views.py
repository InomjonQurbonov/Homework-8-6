from django.shortcuts import render
from rest_framework import viewsets

from app_dictionary.models import Dictionary
from app_dictionary.serializers import DictionarySerializer, GetDictionarySerializer
from app_dictionary.permissions import IsOwnerOrSuperUser


class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    permission_classes = [IsOwnerOrSuperUser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetDictionarySerializer
        return DictionarySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    