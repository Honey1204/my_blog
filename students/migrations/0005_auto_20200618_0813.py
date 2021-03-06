# Generated by Django 3.0.7 on 2020-06-18 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20200618_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsdetail',
            name='cast',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studentsdetail',
            name='father_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studentsdetail',
            name='father_occupation',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studentsdetail',
            name='inter_location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studentsdetail',
            name='intercollege',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studentsdetail',
            name='mother_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studentsdetail',
            name='school',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studentsdetail',
            name='school_location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studentsdetail',
            name='seat_category',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='studentsdetail',
            name='vsat_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentsdetail',
            name='vsat_rank',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='fullstudentdetails',
        ),
    ]
