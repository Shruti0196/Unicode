from django.contrib import admin
from django.urls import path,include
from .views import types
urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/',types,name="type")  
]