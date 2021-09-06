# Django-Task

This is Django based application.In this application basically  CRUD operation is performed.

To use this application.

In Main Project Urls to handle main routes

    path('',include('app.urls')),
    path('api/',include('app.urls_api')),
    path('Rest/',include('app.JwtAuthentication.urls'))
    
    
In App urls there is two section
This app url handles all the CRUD operation 
1 url.py
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.register_view,name='signup'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('logout/',views.logout_view,name='logout'),
    path('delete/<int:id>/',views.delete_view,name='delete')
   
2. url_api.py
  This url handles all the login and registration process
  
   path('login/',view_api.login_api.as_view(),name='login-page'),
   path('register/',view_api.register_api.as_view())
    

JWT Authentication
In JwtAuthentication folder there is url.py file

This url file handels all the api view of whole project


        path('',include(router.urls)),
        path('auth/',include('rest_framework.urls',namespace='rest_framework')),
        path('api/gettoken/',TokenObtainPairView.as_view(),name='gettoken'),
        path('api/refresh/',TokenRefreshView.as_view(),name='gettoken'),

For better experience to use Postman for authentication 
