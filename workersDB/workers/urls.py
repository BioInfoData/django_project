from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('workers', views.WorkerView)
urlpatterns = [
    path('', views.WorkerViewHtml, name = 'workers_list'),
    path('dep/', views.DepartmentViewHtml, name = 'departments_list'),
    path('api/', include(router.urls)),
    path('api-auth', include('rest_framework.urls')),
    path('dep/<slug:slug>/', views.department_detail, name='dep_detail'),
    path('<slug:slug>/', views.worker_detail, name='detail'),


]