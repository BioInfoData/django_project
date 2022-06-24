from rest_framework import serializers
from .models import Worker

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'employee_id', 'first_name','last_name','department_id',
                  'salary','manager_id']