# Generated by Django 5.1 on 2024-09-28 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=30)),
                ('salary', models.IntegerField()),
            ],
            options={
                'verbose_name': 'EmployeeData',
                'verbose_name_plural': 'EmployeeDatas',
            },
        ),
    ]
