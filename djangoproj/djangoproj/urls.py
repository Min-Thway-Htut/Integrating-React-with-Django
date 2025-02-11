from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]

# re_path(r"",views.index,name="index")