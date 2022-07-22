from rest_framework import serializers
from workers.models import Worker

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = [ 'id', 'employee_id', 'first_name','last_name','department_id', 'job_id',
                   'salary','manager_id','commission_pct','email','phone_number','heir_date'
                 ]