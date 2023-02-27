from django.contrib import admin
from django.urls import path
from FormApp import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('insert', views.insert, name='insert'),
    path('admin/', admin.site.urls),
]