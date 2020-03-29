from django.urls import path
from .views import home_view,Registration,login_view
from .views import create_view,detail_view,logout_view,comment_view,comment_delete_view
app_name = 'myapp'
urlpatterns = [
  path("",home_view,name='home'),
  path("registration/",Registration,name='registration'),
  path("login/",login_view,name='login'),
  path("logout/",logout_view,name='logout'),
  path("create/",create_view,name='create'),
  path("article/<int:id>/",detail_view,name='detail'),
  path("comment/<int:article_id>/",comment_view,name='comment'),
  path("deletecomment/<int:comment_id>/",comment_delete_view,name='comment_delete'),
  # path("replycomment/<int:reply_id>/",comment_reply_view,name='comment_reply'),

 
]