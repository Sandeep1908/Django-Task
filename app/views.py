from django.contrib.auth import logout
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from . models import userdata1
from .forms import userform1


def home(request):
    data = userdata1.objects.all()
    if data.count() == 0:
        return render(request, 'app/empty.html', {'data': 'User List is Empty'})
    return render(request, 'app/base.html', {'data': data})


def login_view(request):
    return render(request, 'app/login.html')


def register_view(request):
    return render(request, 'app/register.html')


def edit(request, id):
    if request.user.is_authenticated:

        form = userform1(instance=userdata1.objects.get(id=id))
        if request.method == 'POST':
            fm = userform1(request.POST, instance=userdata1.objects.get(id=id))
            if fm.is_valid():
                fm.save()
                return redirect('/')
        else:
            return render(request, 'app/edit.html', {'form': form})
    else:
        return redirect('/login')


def delete_view(request, id):
    user = userdata1.objects.get(id=id)
    user.delete()
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/login')
