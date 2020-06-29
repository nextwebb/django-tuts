
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('demo/', include('demo.urls')),
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token)

]
