from django.contrib import admin
from .models import signupdata

@admin.register(signupdata)
class signupdisplay(admin.ModelAdmin):
    list_display=('id','name','gender','password','email','phone','active','otp')