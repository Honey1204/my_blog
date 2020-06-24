from django.contrib import admin
from students.models import studentsdetail
# Register your models here.


class studentsdetailAdmin(admin.ModelAdmin):
	#fields is to show only the required things to show in the admin page remaining things will be not shown
	#list display is used to make a table list for thing to show
	list_display = ['Name','email','phone_number','gender','college','Registration_number','branch']
	#to filter the desired result
	# list_filter = ('Name','phone_number','Registration_number')
	# to search 
	search_fields = ['Name']


	# pass
# need to register both the model page and the adminmodel
admin.site.register(studentsdetail,studentsdetailAdmin)


