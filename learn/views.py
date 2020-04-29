from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'learn/learn.html')
# Create your views here.
