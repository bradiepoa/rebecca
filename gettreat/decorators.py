from django.http import HttpResponse
from django.shortcuts import redirect

# allowing aunthenticated users not to access login regester pages

def unauthenticate_user(view_func):
	def wrapper_func(request,*args, **kwargs):
		if request.user.is_authenticated:
			return redirect('gettreat:homepage')
		else:
			return view_func(request,*args, **kwargs)
	return wrapper_func


# allowing usre on supposed pages

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('Your not allowed to view this page')

		return wrapper_func
	return decorator

# redirecting users to the supposed pages

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group =='hospital':
			return redirect('mainweb:hospitapage')

		if group =='patients':
			return redirect('/')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function