from django.core.validators import validate_slug, validate_email
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User

		fields = ['username','email', 'password1', 'password2']


class EmergencyForm(ModelForm):
	class Meta:
		model = Emergency

		fields = '__all__'





class RegisterDoctorForm(ModelForm):
	class Meta:
		model = Our_Doctors

		fields = '__all__'

class DepartmentForm(ModelForm):
	class Meta:

		model = Departments

		fields = '__all__'