from django.contrib import admin
from .models import frienddetail,post
# Register your models here.

@admin.register(frienddetail)
class frienddisplay(admin.ModelAdmin):
    list_display=('id','friendlist','friendrequest','friendrequestsend')

@admin.register(post)
class postdisplay(admin.ModelAdmin):
    list_display=('id','userid','name','article','image')
