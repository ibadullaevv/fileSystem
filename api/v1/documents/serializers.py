from rest_framework import serializers
from django.contrib.auth.models import User

from apps.documents.models import Document


class DocumentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        exclude = ('sender',)


class DocumentListSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.username', read_only=True)
    receiver = serializers.CharField(source='receiver.username', read_only=True)

    class Meta:
        model = Document
        fields = ['id', 'title', 'document', 'description', 'sender', 'receiver', 'created']


class UserListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']