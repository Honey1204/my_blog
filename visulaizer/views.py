from django.shortcuts import render
from .forms import FormDetailsF
from django.contrib import messages
from visulaizer.models import FormDetails
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from visulaizer.serializers import DataSerializer
from django.views.generic import TemplateView
from rest_framework import filters
import csv
from django.http import HttpResponse
# Create your views here.


class HomePageView(TemplateView):
	template_name = "Base.html"

def get_data(request):
	form = FormDetailsF()
	if request.method == 'POST':
		form = FormDetailsF(request.POST)
	if form.is_valid():
		form.save()
		messages.success(request,"successfully uploaded")
	else:
		messages.error(request,"not successfully uploaded")
		form = FormDetailsF()

	return render(request, 'form.html', {'form': form})


def get_table(request):
	obj = FormDetails.objects.all()
	context = {
		'object':obj,
	}
	return render(request,"table.html",context)


	# API's View here 

class CompleteView(ListAPIView):
	queryset = FormDetails.objects.all()
	serializer_class = DataSerializer
	#  there's a filter feacher included in restframework use from rest_framework import filters this to do search
	filter_backends = [filters.SearchFilter]
	# params for search_fields
	# this search_fields is required
	search_fields = ['Unit', 'Date']
	

class DataRetrieve(RetrieveUpdateDestroyAPIView):
	queryset = FormDetails.objects.all()
	serializer_class = DataSerializer
	lookup_field = 'pk'


class FormCreate(CreateAPIView):
	serializer_class = DataSerializer
	queryset = FormDetails.objects.all()




