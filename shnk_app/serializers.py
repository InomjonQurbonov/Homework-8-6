from rest_framework import serializers
from shnk_app.models import Podsystem, Groups, Document, Document_files, Document_types


class PodsystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podsystem
        fields = '__all__'


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document_types
        fields = '__all__'


class Document_filesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document_files
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class GetDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'document_title', 'document_type', 'document_files']
