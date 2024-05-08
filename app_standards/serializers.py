from rest_framework import serializers
from app_standards.models import Standards


class StandardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standards
        fields = '__all__'


class GetStandardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standards
        fields = ['id', 'standard_name', 'standard_number', 'standard_title']
