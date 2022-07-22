from django.db import models
from datetime import date
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Department (models.Model):
    department_id = models.CharField(max_length=100, unique=True)
    description = models.TextField(default="")
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True)

    def save(self, *args, **kwargs):
        super(Department, self).save(*args, **kwargs)
        self.slug = slugify(self.department_id) + "-" + str(self.id)
        return super(Department, self).save(*args, **kwargs)

    def __str__(self):
        return self.department_id

class Worker(models.Model):
    employee_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email =  models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)
    heir_date =models.DateField(default=date.today)
    job_id = models.CharField(max_length=100)
    salary = models.FloatField()
    commission_pct =  models.FloatField()
    manager_id = models.ForeignKey('self', blank=True, null=True, default=0, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    thumb = models.ImageField(blank=True)

    slug = models.SlugField(unique=True, allow_unicode=True, blank=True)

    def save(self, *args, **kwargs):
        super(Worker, self).save(*args, **kwargs)
        self.slug = slugify(self.first_name) + "-" + str(self.id)
        return super(Worker, self).save(*args, **kwargs)

    def __str__(self):
        return self.employee_id
