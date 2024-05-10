from rest_framework import viewsets
from app_standards.models import Standards
from app_standards.serializers import StandardsSerializer, GetStandardsSerializer
from app_standards.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from app_standards.filters import StandardsFilter

from rest_framework.pagination import PageNumberPagination


class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class StandardsViewSet(viewsets.ModelViewSet):
    queryset = Standards.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['standard_title', 'standard_number', 'standard_date']
    filterset_class = StandardsFilter
    pagination_class = StandardPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetStandardsSerializer
        return StandardsSerializer

    def get_queryset(self):
        if 'search' in self.request.GET:
            try:
                return (Standards.objects.filter(
                    standard_title__icontains=self.request.GET['search'])
                        | Standards.objects.filter(standard_name__icontains=self.request.GET['search'])
                        | Standards.objects.filter(standard_number__icontains=self.request.GET['search']))
            except:
                Standards.objects.none()
        return Standards.objects.all()  # Fixed the return statement
