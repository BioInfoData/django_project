from django.shortcuts import render
from .serializers import WorkerSerializer, DepartmentSerializer
from rest_framework import viewsets, permissions
from workers.models import Worker, Department
# Create your views here.


class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class WorkerView(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)

