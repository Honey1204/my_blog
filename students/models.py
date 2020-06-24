from django.db import models

# Create your models here.
class studentsdetail(models.Model):
	Name = models.CharField(max_length=200,null=True)
	Registration_number = models.CharField(max_length=200,null=True)
	branch = models.CharField(max_length=5,null=True)
	college = models.CharField(max_length=200,null=True)
	gender = models.CharField(max_length=40,null=True)
	phone_number = models.CharField(max_length=15,null=True)
	email = models.EmailField(null=True)
	school = models.CharField(max_length=200,null=True)
	school_location = models.CharField(max_length=200,null=True)
	intercollege = models.CharField(max_length=200,null=True)
	inter_location = models.CharField(max_length=200,null=True)
	vsat_rank = models.IntegerField(null=True)
	vsat_marks = models.IntegerField(null=True)
	seat_category = models.CharField(max_length=5,null=True)
	father_name = models.CharField(max_length=200,null=True)
	father_occupation = models.CharField(max_length=200,null=True)
	mother_name = models.CharField(max_length=200,null=True)
	cast = models.CharField(max_length=200,null=True)

	#this returns the name to show in the table
	def __str__(self):
		return self.Name



