from rest_framework import viewsets
from django.db.models import Q

from apps.documents.models import Document
from .serializers import DocumentCreateSerializer, DocumentListSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return DocumentCreateSerializer

        return DocumentListSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Document.objects.all()
        else:
            return Document.objects.filter(
                Q(sender=self.request.user) | Q(receiver=self.request.user)
            )

    def perform_create(self, serializer):
        # Set the sender of the document to be the user making the request
        serializer.save(sender=self.request.user)

        # If the user making the request is not an admin, set the receiver to be the admin
        # if not self.request.user.is_staff:
        #     admin = User.objects.filter(is_staff=True).first()
        #     serializer.save(receiver=admin)
