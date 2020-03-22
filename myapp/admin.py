from django.contrib import admin
from .models import *


admin.site.register([Admin,Visitor,Article,Comment,ReplyComment])
