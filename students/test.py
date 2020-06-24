import json
from students.models import studentsdetail


studentsdetail.objects.all()

with open('/Users/harikach/Desktop/py/tt.json') as file:
	tt = json.load(file)
	for tt in file:
		z =studentsdetail(Registration_number=tt['reg_num'])
		z=studentsdetail(Name=tt['name'])
		z=studentsdetail(branch=tt['branch'])
		z=studentsdetail(gender=tt['gender'])
		z=studentsdetail(college=tt['college'])
		z=studentsdetail(phone_number=tt['Phone_Number'])
		z=studentsdetail(email=tt['Email'])
		z.save()

		z=studentsdetail(Registration_number=tt['reg_num'],Name=tt['name'],branch=tt['branch'],gender=tt['gender'],college=tt['college'],phone_number=tt['Phone_Number'],email=tt['Email'])
