from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    x = datetime.now()
    return render(request, 'birthday/index.html', {
        'date': x.day,
        'month': x.month
    })