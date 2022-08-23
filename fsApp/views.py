from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def home(request):
    # print(request)
    # print(request.method)
    # print(request.COOKIES)
    # print(request.path)
    # print(request.user)
    # # print(request.META)
    # {{ request.user }}
    
    
    # html="<h1>HELLO, i am under the water.</h1>"
    # return HttpResponse(html)
    
def home(request):
    context ={
        'caption': 'clarusway',
        'dict1': {'django':'best Framework'},
        'mylist': [2,3,4]
    }
    return render(request, 'fsApp/index.html', context)