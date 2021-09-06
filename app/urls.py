from django.urls import path
from . import views


urlpatterns=[ 
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.register_view,name='signup'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('logout/',views.logout_view,name='logout'),
    path('delete/<int:id>/',views.delete_view,name='delete')
]
    