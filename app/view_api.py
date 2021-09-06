from django.http.response import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login
from .models import userdata1




class login_api(APIView):
    def post(self,request):
        response={}
        response['status']=500
        response['message']='something went wrong'
        try:
            
            check_user=userdata1.objects.filter(email=request.data.get('email')).first()
           
            if check_user is None:
                response['message']='User not found'
   
            user=authenticate(username=check_user,password=request.data.get('password'))
            
            if user is not None:
                login(request,user)
                response['status']=200
                response['message']='Login susscessfull'
        
        except Exception as e:
            print(e)
        
        return JsonResponse(response)
    

class register_api(APIView):
    def post(self,request):
        response={}
        response['status']=500
        response['message']='Something went wrong'
        
        try:
            data=request.data
            if(data.get('password')==data.get('password2')):
                if userdata1.objects.filter(username=data.get('username')).exists():
                    response['message']='Username already exits'
                    return JsonResponse(response)
                
                if userdata1.objects.filter(email=data.get('email')).exists():
                    response['message']='Eamil already exits'
                    return JsonResponse(response)
                
                user=userdata1.objects.create(username=data.get('username'),email=data.get('email'),Address=data.get('address'))
                user.set_password(data.get('password'))  
                user.save()
                
                
                
                response['message']='Registration done'         
                response['status']=200
            else:
                response['message']='Password doesn\'t matched'
        except Exception as e:
            print(e)
        return JsonResponse(response)


      