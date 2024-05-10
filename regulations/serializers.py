from rest_framework import serializers
from regulations.models import Regulations


class RegulationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regulations
        fields = '__all__'


class GetRegulationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regulations
        fields = ['id', 'reg_sign', 'reg_number', 'reg_title']
