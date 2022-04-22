from django.core.validators import validate_slug, validate_email
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User

		fields = ['username','email', 'password1', 'password2']