from django.urls import path

from . import views

# app_name = 'myTasks'
urlpatterns = [
    path('', views.myTasks, name='myTasks'),
]