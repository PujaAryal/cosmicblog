from django.urls import path
from .views import home_view,Registration,login_view,logout_view

app_name = 'myapp'
urlpatterns = [
  path("",home_view,name='home'),
  path("registration/",Registration,name='registration'),
  path("login/",login_view,name='login'),
  path("logout/",logout_view,name='logout'),
 
]