from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login/index.html')

def create_account(request):
    return render(request, 'create_account/index.html')