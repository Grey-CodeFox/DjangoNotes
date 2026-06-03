from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('hlppp')

def search(request):
    return render(request,'search.html')