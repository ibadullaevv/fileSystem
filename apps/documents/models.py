from django.contrib.auth.models import User
from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=255)
    document = models.FileField()
    description = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
