from django.shortcuts import render, redirect
from django.http import HttpResponse
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
			messages.success(request, 'Emergency request sent successfully')
			return redirect('gettreat:clientspage')
		else:
			messages.error(request, 'Emergency request not sent.. check your form')
			return redirect('gettreat:clientspage')

	context = {'form':form}
	return render(request, 'gettreat/home/clients_infor.html',context)

def LogoutUser(request):
	logout(request)
	return redirect('bookapp:loginpage')


# Client view end of clients views================================================


# hospital views =================================================================

@login_required(login_url='gettreat:homepage')
def Hospitaldash(request):

	emerg = Emergency.objects.all()

	context = {'emerg':emerg}
	return render(request, 'gettreat/hospital/indexhp.html',context)

@login_required(login_url='gettreat:homepage')
def UPdateEmergency(request, pk_emerg):
	emerg = Emergency.objects.get(id=pk_emerg)
	form = EmergencyForm(instance=emerg)

	if request.method == 'POST':
		form = EmergencyForm(request.POST, instance=emerg)
		if form.is_valid():
			form.save()
			messages.error(request, 'Emergency request updated successfully')
			return redirect('gettreat:hospitapage')


	context = {'form':form}
	return render(request, 'gettreat/home/clients_infor.html',context)
	# department
@login_required(login_url='gettreat:homepage')
def DepartmentForm_view(request):

	form = DepartmentForm()
	if request.method == 'POST':
		form = DepartmentForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data.get('Department_Name')
			messages.success(request,'Department registered successfully')
			return redirect('gettreat:hospitapage')

	context= {'form':form}
	return render(request, 'gettreat/hospital/departmentform.html', context)

@login_required(login_url='gettreat:homepage')
def DoctorForm(request):

	form = RegisterDoctorForm()
	if request.method == "POST":
		form = RegisterDoctorForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'Doctor registered successfully')
			return redirect('gettreat:hospitapage')
		else:
			messages.success(request,'Doctor registered successfully')
			return redirect('gettreat:doctors_formpage')
	context = {'form':form}
	return render(request, 'gettreat/hospital/doctors_form.html', context)

@login_required(login_url='gettreat:homepage')
def ListDoctors(request):
	user = request.user
	
	doct = Our_Doctors.objects.filter()
	
	context = {'doct':doct}
	return render(request, 'gettreat/hospital/listdoctors.html',context)


@login_required(login_url='gettreat:homepage')
def UpdateDoctor(request, pk_updd):

	doct = Our_Doctors.objects.get(id=pk_updd)
	form = RegisterDoctorForm(instance=doct)
	if request.method == 'POST':
		form = RegisterDoctorForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			messages.success(request, 'Doctor updated successfully')
			return redirect('gettreat:listdoctorspage')
		else:
			messages.error(request, 'Failed to update, check your form..!!')
			return redirect('gettreat:listdoctorspage')


	context = {'form':form}
	return render(request, 'gettreat/hospital/doctors_form.html', context)

@login_required(login_url='gettreat:homepage')
def AdmittedPatience(request):

	emerg = Emergency.objects.filter(status='admitted')

	context = {'emerg':emerg}
	return render(request, 'gettreat/hospital/admittedpatient.html', context)

@login_required(login_url='gettreat:homepage')
def DeclainedPatients(request):

	emerg = Emergency.objects.filter(status='declined')

	context = {'emerg':emerg}
	return render(request, 'gettreat/hospital/declinedpatints.html', context)


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
				return redirect('gettreat:homepage')
			elif user.is_hospital:
				return redirect('gettreat:homepage')
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


