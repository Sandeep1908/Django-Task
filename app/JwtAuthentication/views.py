from django.http import request
from .serializers import useSerializer
from app.models import userdata1
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class alldata(viewsets.ModelViewSet):
    queryset=userdata1.objects.all()
    serializer_class=useSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

