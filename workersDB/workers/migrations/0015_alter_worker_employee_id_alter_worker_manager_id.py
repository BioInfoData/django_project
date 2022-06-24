# Generated by Django 4.0.5 on 2022-06-24 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0014_alter_worker_manager_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='employee_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='manager_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='workers.worker'),
        ),
    ]
