from django.shortcuts import render,redirect
from django.views.generic import *
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import Admin,Visitor,Article,Comment,ReplyComment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from .forms import RegistrationForm,LoginForm,BlogForm,CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home_view(request):
    articlelist=Article.objects.all()
    form=BlogForm() 
    
    context={
     
     'list':articlelist,
     'form':form,

    }

    return render(request, "home.html",context)


def Registration(request):
	form=RegistrationForm()

	if request.method=='POST':
		form=RegistrationForm(request.POST)

		if form.is_valid():
			a=form.cleaned_data["username"]
			b=form.cleaned_data["email"]
			c=form.cleaned_data["password"]
			user = User.objects.create_user(username=a, email=b, password=c)
			form.instance.user=user
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
            


            user1 = authenticate(request,username=username,password=password)
            print(user1)


            if user1 is not None:
                print(user1)
                
                login(request,user1)
                print('login successfull')
                return HttpResponseRedirect(reverse('myapp:home'))

                
    else:
       loginform=LoginForm()
    return render(request,'login.html',
                {'loginform':loginform,
                  "error": "Invalid username or password"})

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")   

@login_required
def create_view(request):
   form=BlogForm()
   context={}
   if request.method=='POST':
    
    form=BlogForm(request.POST,request.FILES or None)
    if form.is_valid():
        logged_in_user=User.objects.get(username=request.user.username) #Mistake: BlogForm() ko model 'Article' ho jasma ma 'author' vanne field xa 'visitor' vanne xaina ni. tesaile 'form.instance.author' garnu parxa not 'form.instance.visitor'
        visitor = Visitor.objects.get(user=logged_in_user)                        # ani arko kura author ma 'Visitor' ko object pathaunu parxa kina ki author has foreign key with Visitor.
                                                                                  # ani 'Visitor' ma feri foreign key 'user' lai garya xa teivaera paila tyo 'user' object tannu parxa teskai lagi 'logged_in_user=User.objects.get(username=request.user.username)' garya ho.
                                                                                  # ani tmle banako models haru anushar user register vaesakepaxi tyei user lai Visitor ma gayera ni banauna parxa.
        form.instance.author=visitor
        form.save()       
        return redirect("myapp:home")
    else:
        print("user not found")    

   else:
    form=BlogForm()
   return render(request,'create.html',{'form':form})     
   

@login_required
def detail_view(request,id):
  form=CommentForm()
  article=Article.objects.get(id=id)
  comment=Comment.objects.filter(article=id)
  context={
   'article':article,
   'comments':form,
   'commentss':comment,
  }

  return render(request,'detail.html',context)



@login_required
def comment_delete_view(request,comment_id):
  commment_delete = Comment.objects.get(id=comment_id)
  commenter=commment_delete.commenter
  print(commenter)
  articl_id=commment_delete.article.id
  print(articl_id)
  
  if request.user.is_authenticated and request.user == commenter.user:
    commment_delete.delete()
    print('comment deleted...')
  else:
    print('user is not the commenter') 
    
  return HttpResponseRedirect(reverse('myapp:detail',kwargs={'id':articl_id}))    
  
      # print(commment_delete)





@login_required
def comment_view(request,article_id):
  form=CommentForm()
  

  if request.method=='POST':
    form=CommentForm(request.POST)

    if form.is_valid():
      form.instance.article=Article.objects.get(id=article_id)
      logged_in_user=User.objects.get(username=request.user.username)
      visitor=Visitor.objects.get(user=logged_in_user)
      form.instance.commenter=visitor
      
      
      form.save()
      return HttpResponseRedirect(reverse('myapp:detail',kwargs={'id':article_id}))
      
  else:
      form=CommentForm()
      article=Article.objects.get(id=article_id)
      context = {
        'form':form,
        'article':article,
            
        } 

  return render(request,"detail.html",context)


# @login_required
# class comment_reply_view(request,reply_id):
#   form=ReplyForm()

#   if request.method=='POST':
#     form=ReplyForm(request.POST)

#     if form.is_valid():
#       form.instance.article=Article.objects.get(id=reply_id)
#       logged_in_user=User.objects.get(username=request.user.username)
#       visitor=Visitor.objects.get(user=logged_in_user)
#       form.instance.commenter=visitor

      
      
#       form.save()
#       return HttpResponseRedirect(reverse('myapp:detail',kwargs={'id':reply_id}))
#   else:
#       form=ReplyForm() 
#       context={
#        'form':form
#       }   

#   return render(request,"detail.html",context)




   
