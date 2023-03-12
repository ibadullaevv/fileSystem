from rest_framework import serializers

from apps.documents.models import Document


class DocumentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'document', 'description', 'receiver', 'created']


class DocumentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'document', 'description', 'sender', 'receiver', 'created']
