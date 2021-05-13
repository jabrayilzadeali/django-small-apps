from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('writeHello', views.writeHello, name='writeHello'),
    path('theButtonPage/', views.theButtonPage, name="theButtonPage"),
    path('ultrapage/', views.ultrapage, name="ultrapage"),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('', views.index, name="index"),
]