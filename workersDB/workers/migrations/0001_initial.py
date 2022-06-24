# Generated by Django 4.0.5 on 2022-06-22 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=100)),
                ('hier_date', models.CharField(max_length=100)),
                ('job_id', models.CharField(max_length=100)),
                ('salary', models.FloatField()),
                ('commission_pct', models.FloatField()),
                ('manager_id', models.IntegerField()),
                ('department_id', models.IntegerField()),
                ('slug', models.SlugField()),
            ],
        ),
    ]
