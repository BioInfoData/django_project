# Generated by Django 4.0.5 on 2022-06-24 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0013_alter_worker_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='manager_id',
            field=models.CharField(max_length=100),
        ),
    ]