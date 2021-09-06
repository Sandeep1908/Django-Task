
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('api/',include('app.urls_api')),
    path('Rest/',include('app.JwtAuthentication.urls'))
]
