from django.shortcuts import render
from signup.models import signupdata as User
from django.http import HttpResponseRedirect,JsonResponse
import json
from .models import frienddetail,post

def getusername(id):
    name=User.objects.get(id=id).__dict__['name']
    return name

def homeview(request):
    if request.session.get('userid','DEFAULT') !="DEFAULT":
        friend=[]
        friendlist=[]
        count=0
        if frienddetail.objects.filter(id=request.session.get('userid')).exists():
            friend=frienddetail.objects.get(id=request.session.get('userid'))
            if friend.friendrequest:
                count=len(friend.friendrequest)
            if friend.friendlist:
                friendlist=friend.friendlist
            friendlist=[i[0] for i in friendlist]
        article=post.objects.filter(userid__in=friendlist).order_by('-id')
        context={'post':article,'friend':friend,'count':count}
        return render(request, 'home.html', context )
    else:
        return HttpResponseRedirect('/login/')

def searchview(request):
    if request.session.get('userid','DEFAULT') !="DEFAULT":
        if request.method=="POST":
            name=request.POST['name']
            friendlist=friend=friendrequest=friendrequestsend=0
            if frienddetail.objects.filter(id=request.session.get('userid')).exists():
                    detail=frienddetail.objects.get(id=request.session.get('userid'))
                    friend=detail.friendlist
                    friendrequestsend=detail.friendrequestsend
                    friendrequest=detail.friendrequest
            if '@' in name:
                friendlist=User.objects.filter(email__startswith=name).exclude(id=request.session.get('userid')).defer('password','otp','active').order_by('name').values()
            elif name.isdigit():
                friendlist=User.objects.filter(phone__startswith=name).exclude(id=request.session.get('userid')).defer('password','otp','active').order_by('name').values()
            else:
                friendlist=User.objects.filter(name__startswith=name).exclude(id=request.session.get('userid')).defer('password','otp','active').order_by('name').values()
            friendlist=list(friendlist)
            return JsonResponse({'friendlist':friendlist,'friend':friend,'friendrequestsend':friendrequestsend,'friendrequest':friendrequest})

def savepost(request):
    if request.session.get('userid','DEFAULT') !="DEFAULT":
        if request.method=="POST":
            name=getusername(request.session.get('userid'))
            if 'article' in request.POST.keys():
                article=request.POST['article']
                image=0   
            elif 'image' in request.POST.keys():
                image=request.POST['image']
                article=0
            else:
                return JsonResponse({'status':0})    
            reg=post(userid=request.session.get('userid'),name=name,article=article,image=image)
            reg.save()  
            return JsonResponse({'status':1})

def sendrequest(request):
    if request.session.get('userid','DEFAULT') !="DEFAULT":
        if request.method=="POST":
            try:
                    frequest=[str(request.session.get('userid')),getusername(request.session.get('userid'))]
                    if frienddetail.objects.filter(id=request.POST['id']).exists():
                        detail=frienddetail.objects.get(id=request.POST['id'])
                        if 'response' in request.POST:
                            if frequest in detail.friendrequestsend:
                                detail.friendrequestsend.remove(frequest)
                            if frequest in detail.friendrequest:
                                detail.friendrequest.remove(frequest)
                            if request.POST['response']=='1':
                                detail.friendlist.append(frequest)
                        else:
                            detail.friendrequest.append(frequest)
                        detail.save()
                    else:
                        reg=frienddetail(id=request.POST['id'],friendrequest=[frequest],friendlist=[],friendrequestsend=[])
                        reg.save() 
                    frequest=[request.POST['id'],request.POST['name']]
                    if frienddetail.objects.filter(id=request.session.get('userid')).exists():
                        detail=frienddetail.objects.get(id=request.session.get('userid'))
                        if 'response' in request.POST:
                            if frequest in detail.friendrequestsend:
                                detail.friendrequestsend.remove(frequest)
                            if frequest in detail.friendrequest:
                                detail.friendrequest.remove(frequest)
                            if request.POST['response']=='1':
                                detail.friendlist.append(frequest)
                        else:
                            detail.friendrequestsend.append(frequest)
                        detail.save()
                        friendrequest=detail.friendrequest
                        friendrequestsend=detail.friendrequestsend
                        friend=detail.friendlist
                    else:
                        reg=frienddetail(id=request.session.get('userid'),friendrequest=[],friendlist=[],friendrequestsend=[frequest])
                        reg.save()
                        friendrequest=[]
                        friendrequestsend=frequest
                        friend=[]
                    return JsonResponse({'status':1,'friend':friend,'friendrequestsend':friendrequestsend,'friendrequest':friendrequest})
            except:
                    return JsonResponse({'status':0}) 

def friendprofile(request,id):
    if request.session.get('userid','DEFAULT') !="DEFAULT":
        user=User.objects.get(id=id).__dict__
        [user.pop(key) for key in ['password','otp','active','_state','id']]
        article=post.objects.filter(userid=id).order_by('-id')
        userfriend=0
        friend=0
        count=0
        if frienddetail.objects.filter(id=request.session.get('userid')).exists():
            userfriend=frienddetail.objects.get(id=request.session.get('userid')).__dict__['friendlist']
            userfriend.sort(key = lambda x: x[1])
        if frienddetail.objects.filter(id=id).exists():
            friend=frienddetail.objects.get(id=id).__dict__['friendlist']
            friend.sort(key = lambda x: x[1])
        context={'post':article,'friend':friend,'userfriend':userfriend,'user':user}
        return render(request, 'profile.html', context )
    else:
        return HttpResponseRedirect('/login/')