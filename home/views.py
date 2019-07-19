from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
   return	render(request,	'homes/base.html')

def second(request):
    return HttpResponse("Second page")
