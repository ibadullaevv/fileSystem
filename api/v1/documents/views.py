from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.db.models import Q

from apps.documents.models import Document
from .serializers import DocumentCreateSerializer, DocumentListSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all().order_by('-created')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve', 'update', 'destroy'):
            return DocumentListSerializer
        return DocumentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Document.objects.all()
        else:
            return Document.objects.filter(Q(sender=user) or Q(receiver=user))


class AdminFileUploadView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        file = request.FILES.get('document')
        if not file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
        receiver = request.user
        sender_id = request.data.get('sender_id')
        if not sender_id:
            return Response({'error': 'No sender provided'}, status=status.HTTP_400_BAD_REQUEST)
        # sender = CustomUser.objects.get(id=sender_id)
        sender = User.objects.get(id=sender_id)
        new_file = Document.objects.create(title=file.title, document=file, sender=sender, receiver=receiver)
        return Response(DocumentListSerializer(new_file).data, status=status.HTTP_201_CREATED)
