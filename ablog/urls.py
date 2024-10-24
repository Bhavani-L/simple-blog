
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('members.urls')),
]
