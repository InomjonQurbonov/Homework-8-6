from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from user.models import Contacts

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'last_name', 'email', 'date_joined', 'last_login')
        read_only_fields = ('date_joined', 'last_login')


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class GetContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'full_name', 'email', 'message', 'for_leadership']
