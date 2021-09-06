from django.db import router
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router=DefaultRouter()
router.register('userapi',views.alldata,basename='userdata')

urlpatterns=[
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('api/gettoken/',TokenObtainPairView.as_view(),name='gettoken'),
    path('api/refresh/',TokenRefreshView.as_view(),name='gettoken'),
    

]