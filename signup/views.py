from django.shortcuts import render
from .form import signupform
from .models import signupdata as User
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib import messages

def signupview(request):
    if request.session.get('userid','DEFAULT') =="DEFAULT":
        if request.method == 'POST':
            form = signupform(request.POST)
            if form.is_valid():
                userObj = form.cleaned_data
                username = userObj['name']
                email =  userObj['email']
                password =  userObj['password']
                gender=userObj['gender']
                phone=userObj['phone']
                reg=User(name=username,email=email, password=password,phone=phone,gender=gender)
                reg.save()
                messages.info(request, 'Account Created Sucessfully')
                return HttpResponseRedirect('/login/')
            else:
                return render(request, 'signup.html', {'form' : form})    
        else:
            form = signupform()
            return render(request, 'signup.html', {'form' : form})
    else:
        form = signupform()
        return render(request, 'signup.html', {'form' : form})

def validateview(request):
    if request.method=="POST":
        data,value=request.POST.items()
        if User.objects.filter(**{data[0]:data[1]}).exists():
            return JsonResponse({'status':0})
        else:
            return JsonResponse({'status':1})
