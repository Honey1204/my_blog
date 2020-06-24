from django.contrib import admin
from django.urls import path,include
from visulaizer.views import get_data,get_table,DataRetrieve,HomePageView,FormCreate,CompleteView

urlpatterns = [
	path('ss/',get_data),
	path('table/',get_table),
	path('api-data/fulldata/',CompleteView.as_view(),name='fulldata'),
	path('api-data/view/<int:pk>/',DataRetrieve.as_view(),name='dataview'),
	path('api-data/create/',FormCreate.as_view(),name='formcreate'),
	path('Home/',HomePageView.as_view()),
	path('',HomePageView.as_view()),

]
