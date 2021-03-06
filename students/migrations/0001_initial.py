# Generated by Django 3.0.7 on 2020-06-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentsdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Registration_number', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=5)),
                ('school', models.CharField(max_length=200)),
                ('school_location', models.CharField(max_length=200)),
                ('inter_marks', models.CharField(max_length=200)),
                ('intercollege', models.CharField(max_length=200)),
                ('inter_location', models.CharField(max_length=200)),
                ('vsat_rank', models.CharField(max_length=200)),
                ('vsat_marks', models.CharField(max_length=200)),
                ('seat_category', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('father_occupation', models.CharField(max_length=200)),
                ('mother_name', models.CharField(max_length=200)),
                ('cast', models.CharField(max_length=200)),
            ],
        ),
    ]
