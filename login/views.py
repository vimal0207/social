from django.shortcuts import render
from .form import loginform
from signup.models import signupdata as User
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect

def loginview(request):
    if request.session.get('userid','DEFAULT') =="DEFAULT":
        if request.method=="POST":
            form = loginform(request.POST)
            userid=form.data['userid']
            pasw=form.data['password']
            if userid.isdigit():
                if(User.objects.filter(phone=userid,password=pasw)).exists():
                    userid=User.objects.get(phone=userid,password=pasw).__dict__['id']
                    request.session['userid']=userid
                    return HttpResponseRedirect('/home/') 
                else:
                    print(2)
                    messages.info(request, 'Invalid Userid')
            else:
                if(User.objects.filter(email=userid,password=pasw)).exists():
                    userid=User.objects.get(email=userid,password=pasw).__dict__['id']
                    request.session['userid']=userid
                    return HttpResponseRedirect('/home/') 
                else:
                    print(3)
                    messages.info(request, 'Invalid Userid')
            return render(request, 'login.html' , {'form':form})
        else:
            form=loginform()
            return render(request, 'login.html' , {'form':form})
    else:
        return HttpResponseRedirect('/home/')

def logout(request):
    if request.session.get('userid','DEFAULT') !="DEFAULT":
        request.session.flush()
        return HttpResponseRedirect( "/home/")
    else:
        return HttpResponseRedirect( "/home/")