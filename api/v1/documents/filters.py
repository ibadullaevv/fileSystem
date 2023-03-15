from django_filters import rest_framework

from apps.documents.models import Document


class DocumentFilter(rest_framework.FilterSet):
    title = rest_framework.CharFilter(lookup_expr='icontains')
    receiver__username = rest_framework.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Document
        fields = ['title']