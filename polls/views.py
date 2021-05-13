from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name')

def index(request):
    myHTML = """
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Index page</title>
                    <style>
                        body {
                            margin: 0;
                        }

                        h1 {
                            background-color: black;
                            padding: 15px;
                            margin: 0;
                            color: white;
                            text-align: center;
                        }

                        h2 {
                            margin: 15px;
                            padding: 15px;
                        }

                        ul {
                            list-style-type: none;

                        }

                        a {
                            text-decoration: none;
                        }

                        a:hover {
                            color: red;
                        }
                    </style>
                </head>

                    <h1>Welcome to my World, Django!!</h1>
                    <h2> this is the first page</h2>
                    <ul>
                        <li><a href="/">go back to the main page</a></li>
                        <li><a href="/polls/ultrapage">go to the ultrapage</a></li>
                        <li><a href="/polls/theButtonPage">The button page</a></li>
                    </ul>
                </body>
            </html>
        """
        # hello how are you my friend okay:W
        
    return HttpResponse(myHTML)


tasks = []
def ultrapage(request):
    print(tasks)
    return render(request, 'polls/myUltrapage.html', {
        'ultratasks': tasks
    })

def add(request):
    # print(request.POST)
    if request.method == "POST":
        myTask = request.POST['yourTask']
        print(request.POST)
        # print(f'<<<<<< <<<<<<<<<<<<  yes it is a POST request {myTask}')
        tasks.append(myTask)
        # print(tasks)
        # return render(request, 'polls/myUltrapage.html', {
        #     'ultratasks': tasks
        # }) # if I use render when I refresh the page it will add myTask again the tasks
        return HttpResponseRedirect(reverse('polls:ultrapage')) # if I use this method it will not add
    else:
        print(f'>>>>>>>>>>>> >>>>>> yes it is a GET request {request.GET}')
        # tasks.append[]

    return render(request, 'polls/add.html')

def delete(request):
    global tasks
    if request.POST:
        tasks = []
        return render(request, 'polls/myUltrapage.html', {
            'ultratasks': tasks
        })
    return render(request, 'polls/delete.html')


def theButtonPage(request):
    return render(request, 'polls/theButtonPage.html')

def writeHello(request):
    return HttpResponseRedirect(reverse('polls:theButtonPage', {
        'hello': 'hello html button to my django world'
    }))