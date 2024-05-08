from rest_framework import serializers
from app_leadership.models import Leadership, StructuralUnits


class StructuralUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StructuralUnits
        fields = '__all__'


class GetStructuralUnits(serializers.ModelSerializer):
    class Meta:
        model = StructuralUnits
        fields = ['id', 'department_name', 'boss_full_name', 'boss_email', 'boss_phone_number']


class LeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = '__all__'


class GetLeadership(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = ['id', 'leader_full_name', 'leader_position', 'leader_Works_days']
