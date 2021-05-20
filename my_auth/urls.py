from django.urls import path

from . import views

app_name = "my_auth"
urlpatterns = [
    path('', views.login, name='login'),
    path('create_account/', views.create_account, name='create_account'),
]