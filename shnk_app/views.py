from rest_framework import viewsets

from shnk_app.models import Podsystem, Groups, Document, Document_files, Document_types
from shnk_app.serializers import (
    PodsystemSerializer, GroupsSerializer,
    DocumentSerializer, GetDocumentSerializer,
    DocumentTypeSerializer, Document_filesSerializer
)
from shnk_app.permissions import IsAdminOrReadOnly


class PodsystemViewSet(viewsets.ModelViewSet):
    queryset = Podsystem.objects.all()
    serializer_class = PodsystemSerializer
    permission_classes = [IsAdminOrReadOnly]


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = [IsAdminOrReadOnly]


class DocumentTypesViewSet(viewsets.ModelViewSet):
    queryset = Document_types.objects.all()
    serializer_class = DocumentTypeSerializer
    permission_classes = [IsAdminOrReadOnly]


class DocumentFilesViewSet(viewsets.ModelViewSet):
    queryset = Document_files.objects.all()
    serializer_class = Document_filesSerializer
    permission_classes = [IsAdminOrReadOnly]


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetDocumentSerializer
        return DocumentSerializer
