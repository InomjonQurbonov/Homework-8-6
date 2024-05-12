from rest_framework import viewsets
from app_leadership.models import Leadership, StructuralUnits
from app_leadership.serializers import (
    LeadershipSerializer, StructuralUnitsSerializer,
    GetLeadership, GetStructuralUnits
)
from app_leadership.permissions import IsAdminOrReadOnly


class LeadershipViewSet(viewsets.ModelViewSet):
    queryset = Leadership.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetLeadership
        return LeadershipSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = StructuralUnits.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetStructuralUnits
        return StructuralUnitsSerializer
