import django_filters
from app_standards.models import Standards


class StandardsFilter(django_filters.FilterSet):
    class Meta:
        model = Standards
        fields = ['standard_title', 'standard_number', 'standard_date']
