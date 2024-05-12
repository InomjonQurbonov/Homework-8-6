from rest_framework import serializers
from app_dictionary.models import Dictionary


class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'


class GetDictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ['id', 'dict_number', 'word_uzb', 'word_meaning']
