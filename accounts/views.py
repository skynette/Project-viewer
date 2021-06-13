from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from core.views import check_paid


def register(request):
	if request.method == "POST" and request.FILES['pic']:
		if request.POST['email'] and request.POST['about'] and request.POST['twitter'] and request.POST['facebook'] and request.POST['password1'] and request.POST['password2'] and request.POST['first_name'] and request.POST['last_name'] and request.FILES['pic']:
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			username = request.POST['email']
			about = request.POST['about']
			twitter = request.POST['twitter']
			facebook = request.POST['facebook']
			password = request.POST['password1']
			password2 = request.POST['password2']
			pic = request.FILES['pic']

		if User.objects.filter(username=username).exists():
			messages.error(request, 'Email already taken')
			print("EMAIL TAKEN ERROR")
			return redirect('register')
		elif password != password2:
			print("PASWWORD ERRIR")
			messages.error(request, 'Passwords do not match')
			return redirect('register')
		else:
			user = User.objects.create_user(username=username, password=password, email=username, first_name=first_name, last_name=last_name)
			user.save()
			profile = Profile.objects.create(
				user=user, picture=pic, about=about, twitter=twitter, facebook=facebook)
			profile.save()
			messages.success(request, 'Account created')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('initiate-payment')

	context = {

	}
	return render(request, 'register_.html', context)

def login_view(request):	
	if request.method == "POST":
		username = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			if check_paid(request.user):
				messages.success(request, 'Successfully logged in')
			else:
				return redirect('initiate-payment')
			# messages.success(request, 'Welcome '+ user.first_name)
		else:
			messages.error(request, 'Invalid credentials')
			return redirect('login')
		return redirect('/')
	context = {

	}
	return render(request, 'login.html', context)

@login_required(login_url="login")
def logout_view(request):
	logout(request)
	messages.success(request, 'You have been logged out')
	return redirect('login')
