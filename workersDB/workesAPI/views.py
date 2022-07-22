from django.shortcuts import render
from .serializers import WorkerSerializer
from rest_framework import viewsets, permissions
from workers.models import Worker
# Create your views here.

class WorkerView(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
