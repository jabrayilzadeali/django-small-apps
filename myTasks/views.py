from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your views here.
class myForms(forms.Form):
    f = forms.CharField(label="New Task")


def myTasks(request):
    form = myForms()
    if "tasks" not in request.session:
        request.session["tasks"] = []
    if request.POST:
        if 'add_task' in request.POST:
            print(f"this is the post method: {request.POST['f']}")
            print(request.session['tasks'])
            request.session['tasks'] += [request.POST['f']] # if we use don't convert it to list(request.POST['f']) it will add all indivial characters to the list not strings
            print(request.session['tasks'])
            return HttpResponseRedirect(reverse('myTasks'))
        elif 'delete_task' in request.POST:
            print('hello multiple forms --------------------')
            request.session['tasks'] = []
            return HttpResponseRedirect(reverse('myTasks'))
    else:
        return render(request, 'myTasks/index.html' ,{
            'form': form,
            'tasks': request.session['tasks']
        })
