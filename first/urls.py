
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('demo/', include('demo.urls')),
    path('admin/', admin.site.urls),

]
