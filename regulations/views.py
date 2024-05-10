from rest_framework import viewsets

from regulations.models import Regulations
from regulations.permissions import IsAdminOrReadOnly
from regulations.serializers import RegulationsSerializer, GetRegulationsSerializer


class RegulationsViewSet(viewsets.ModelViewSet):
    queryset = Regulations.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetRegulationsSerializer
        return RegulationsSerializer
