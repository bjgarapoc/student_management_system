# Generated by Django 4.2.13 on 2024-05-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=4)),
                ('gender', models.CharField(max_length=6)),
                ('age_start', models.IntegerField()),
                ('age_end', models.IntegerField()),
            ],
        ),
    ]
