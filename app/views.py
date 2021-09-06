# from django.contrib.auth import logout
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView
from . models import userdata
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


def home(request):
    data=userdata.objects.all()
    if data.count()==0:
        return render(request,'app/empty.html',{'data':'User List is Empty'})
    return render(request,'app/base.html',{'data':data})
    
        

def login_view(request):
    return render(request, 'app/login.html')


def register_view(request):
    return render(request, 'app/register.html')

def edit(request,id):
    if request.user.is_authenticated:
    
        data=userdata.objects.get(id=id)
        user=User.objects.get(id=data.user.id)

        if request.method=='POST':
            username=request.POST['username']
            email=request.POST['email']
            address=request.POST['address']
            user.username=username
            user.email=email
            user.save()
            data.Address=address
            data.save()
            return redirect('/')
         
        else:
             return render(request,'app/edit.html',{'form':data})
    else:
        return redirect('/login')


def delete_view(request,id):
    data=userdata.objects.get(id=id)
    user=User.objects.get(id=data.user.id)
    user.delete()
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/login_view')




