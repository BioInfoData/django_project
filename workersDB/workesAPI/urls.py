from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('workers', views.WorkerView)
router.register('dep', views.DepartmentView)
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth', include('rest_framework.urls')),
]