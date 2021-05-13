from django.urls import path

from . import views

app_name = 'change_color'
urlpatterns = [
    path('', views.index, name='index'),
    path('black/', views.black, name='black'),
    path('green/', views.green, name='green'),
    path('red/', views.red, name='red'),
]