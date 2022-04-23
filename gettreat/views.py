from django.shortcuts import render, redirect
# login
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login,logout

# restrict users
from django.contrib.auth.decorators import login_required

# import decorator
from.decorators import unauthenticate_user

from.models import *
from.forms import*

# Create your views here.

# Client view================================================
def Homeview(request):
	
	return render(request ,'gettreat/home/index.html')


def Contactview(request):

	return render(request ,'gettreat/home/contact.html')


def Serviceview(request):

	return render(request ,'gettreat/home/services.html')


def Aboutview(request):

	return render(request ,'gettreat/home/about.html')

@login_required(login_url='gettreat:homepage')
def Clientsview(request):
	form = EmergencyForm()
	if request.method == 'POST':
		form = EmergencyForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('gettreat:clientspage')

	context = {'form':form}
	return render(request, 'gettreat/home/clients_infor.html',context)


# Client view end of clients views================================================


# hospital views =================================================================

@login_required(login_url='gettreat:homepage')
def Hospitaldash(request):
	return render(request, 'gettreat/hospital/indexhp.html')



# end of hopital views=============================================================




# admin=====================================

@login_required(login_url='gettreat:homepage')
def dashboard(request):

	hopit = Hospital.objects.all()

	patients = Our_Patients.objects.all()


	context ={'hopit':hopit, 'patients':patients}
	return render(request ,'gettreat/admin/index.html', context)

@login_required(login_url='gettreat:homepage')
def EmergencyRequest(request):

	hopit = Hospital.objects.all()

	emerg = Appointments.objects.all()

	context ={'hopit':hopit, 'emerg':emerg}
	return render(request, 'gettreat/admin/emergency.html', context)

@login_required(login_url='gettreat:homepage')
def HospitalDetails(request):

	hopit = Hospital.objects.all()

	context ={'hopit':hopit}
	return render(request, 'gettreat/admin/hospital_datails.html', context)

# end of admin=====================================

# Aunthentication process====================================================
@unauthenticate_user
def Loginview(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request,user)
			if user.is_admin  or user.is_superuser:
				return redirect('gettreat:dashboardpage')
			elif user.is_hospital:
				return redirect('gettreat:hospitapage')
			else:
				return redirect('gettreat:homepage')
		else:
			messages.info(request, "Invalid Username or Password")
			return redirect('gettreat:loginpage')
	return render(request, 'gettreat/register/login.html')

@login_required(login_url='gettreat:homepage')
def logoutUser(request):
	logout(request)
	return redirect('gettreat:homepage')

@unauthenticate_user
def Registeriew(request):
	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			messages.success(request,'Account was Created for ' + user)
			return redirect('gettreat:loginpage')

	context = {'form':form}
	return render(request, 'gettreat/register/register.html',context)


