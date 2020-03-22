from django.shortcuts import render,redirect
from django.views.generic import *
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Admin,Visitor,Article,Comment,ReplyComment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from .forms import RegistrationForm,LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home_view(request):
	context={}

	return render(request, "home.html",context)


def Registration(request):
	form=RegistrationForm()

	if request.method=='POST':
		form=RegistrationForm(request.POST)

		if form.is_valid():
			a=form.cleaned_data["username"]
			b=form.cleaned_data["email"]
			c=form.cleaned_data["password"]
			puja_user = User.objects.create_user(a, c, b)
			form.instance.user=puja_user
			form.save()
			return redirect('myapp:login')

	else:
		form=RegistrationForm()
		return render(request,"registration.html",{'form':form})

def login_view(request): 

    loginform=LoginForm()
    if request.method=='POST':
        loginform=LoginForm(request.POST,request.FILES or None)
        if loginform.is_valid():
         	
         username = loginform.cleaned_data['username']
         password = loginform.cleaned_data['password']
         print(username)
         print(password)

         user = authenticate(request,username=username,password=password)
         print(user)

         if user:
            login(request,user)
            print('login successfull')
            return HttpResponseRedirect(reverse('myapp:home'))

                
    else:
       loginform=LoginForm()
       return render(request,'login.html',{'loginform':loginform})

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")       