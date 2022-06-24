from django.shortcuts import render
from .models import Worker, Department
from .serializers import WorkerSerializer
from rest_framework import viewsets, permissions

class WorkerView(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)

def WorkerViewHtml(request):
    workers = Worker.objects.all()
    return render(request, 'index.html', {'workers': workers})

def worker_detail(request,slug):
    worker = Worker.objects.get(slug=slug)
    return render(request, "worker_details.html", {'worker': worker})

def department_detail(request,slug):
    department = Department.objects.get(slug=slug)
    return render(request, "department_details.html", {'department': department})

def DepartmentViewHtml(request):
    departments = Department.objects.all()
    return render(request, 'departments_list.html', {'departments': departments})
