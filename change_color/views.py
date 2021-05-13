from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'change_color/index.html')

def black(request):
    return render(request, 'change_color/black.html')

def green(request):
    return render(request, 'change_color/green.html')

def red(request):
    return render(request, 'change_color/red.html')