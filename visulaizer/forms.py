from django import forms
from visulaizer.models import FormDetails

class FormDetailsF(forms.ModelForm):
	class Meta:
		model = FormDetails
		fields = '__all__'
