from django.db import models
from django.forms import ModelForm

# Create your models here.


class FormDetails(models.Model):
	UNIT_CHOICES = (
		('U1','UNIT 1'),
		('U2','UNIT 2'),
		('U3','UNIT 3'),
		)
	Date = models.DateField()
	Unit = models.CharField(max_length=30,choices=UNIT_CHOICES,null=True)
	Blowroom = models.IntegerField(null=True)
	Waste_Collection = models.IntegerField(null=True)
	Carding = models.IntegerField(null=True)
	Comber_Drawing = models.IntegerField(null=True)
	Speed_Frame = models.IntegerField(null=True)
	Pre_Total = models.IntegerField(null=True)
	Spg_DB1 = models.IntegerField(null=True)
	Spg_DB2 = models.IntegerField(null=True)	
	Spg_DB3 = models.IntegerField(null=True)
	Spg_DB4 = models.IntegerField(null=True)
	Spg_Total = models.IntegerField(null=True)
	Autoconner = models.IntegerField(null=True)
	Post_spinning_total = models.IntegerField(null=True)
	Pre_HMD = models.IntegerField(null=True)
	Spg1_HMD = models.IntegerField(null=True)
	Spg2_HMD = models.IntegerField(null=True)
	Post_Spg_HMD = models.IntegerField(null=True)
	Total = models.IntegerField(null=True)
	Compressor = models.IntegerField(null=True)
	Lighting = models.IntegerField(null=True)
	Total_Units = models.IntegerField(null=True)
	Production = models.IntegerField(null=True)
	UKG = models.IntegerField(null=True)
	s40s_con_pro = models.IntegerField(null=True)
	s40s_Con_Ukg = models.IntegerField(null=True)
	s40s_Compac_con_pr = models.IntegerField(null=True)
	s40s_Compac_con_ukg = models.IntegerField(null=True)

	def __str__(self):
		return self.Unit



# class FormDetailsF(ModelForm):
# 	class Meta:
# 		model = FormDetails
# 		fields = ['Date','Unit','Blowroom','Waste_Collection',]




