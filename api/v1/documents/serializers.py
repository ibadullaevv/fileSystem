from django.contrib.auth.models import User
from rest_framework import serializers

from apps.documents.models import Document


class DocumentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'document', 'description', 'receiver', 'created']

    # def __init__(self, *args, **kwargs):
    #     current_user = kwargs.pop('sender', None)
    #     super().__init__(*args, **kwargs)
    #     if current_user:
    #         self.fields['receiver'].queryset = User.objects.exclude(pk=current_user.pk)
    #
    # def save(self, commit=True, *args, **kwargs):
    #     instance = super().save(commit=False)
    #     instance.sender = kwargs.pop('sender')
    #     if commit:
    #         instance.save()
    #     return instance


class DocumentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'document', 'description', 'sender', 'receiver', 'created']
