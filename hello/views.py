from django.shortcuts import render
from django.utils.timezone import datetime
# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )