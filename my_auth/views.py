from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import Accounts

# Create your views here.
class CreateAccount(forms.Form):
    username = forms.CharField(label="Username", max_length=64)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ('confirm_password')


class Login(forms.Form):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Your Email")
    password = forms.CharField(widget=forms.PasswordInput, label="your password")


def login(request):
    form = Login()
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if username in list(Accounts.objects.values_list("username", flat=True)):
                actual_password = Accounts.objects.filter(username=username).first().password
                actual_email = Accounts.objects.filter(username=username).first().email
                print('-----------------------------------------------------------------------------------------')
                print(actual_password, username)
                if password == actual_password and email == actual_email:
                    print('passwords are match')
                    return render(request, 'login/user.html', {
                        'user': username
                    })
                print('hello I am here')
                print(email, password) ########################################################################Look Here
    return render(request, 'login/index.html', {
        'forms': form
    })

def create_account(request):
    if request.method == "POST":
        form = CreateAccount(request.POST)
        # print('============================================================POST============================================================')
        # print(form)
        # print('============================================================POST============================================================')
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['password_again']
            # print(username, email, password, confirm_password)
            if password == confirm_password:
                my_account = Accounts(username = username, email = email, password = password)
                my_account.save()
                return HttpResponseRedirect(reverse("my_auth:login"))
            else:
                print('password are not match')
                if password != confirm_password:
                    raise forms.ValidationError(
                        "password and confirm_password does not match"
                    )
    else:
        form = CreateAccount()
            
    return render(request, 'create_account/index.html', {
        'forms': form
    })