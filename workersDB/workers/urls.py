from django.urls import path
from . import views



urlpatterns = [
    path('', views.WorkerViewHtml, name = 'workers_list'),
    path('dep/', views.DepartmentViewHtml, name = 'departments_list'),
    path('dep/<slug:slug>/', views.department_detail, name='dep_detail'),
    path('<slug:slug>/', views.worker_detail, name='detail'),
]