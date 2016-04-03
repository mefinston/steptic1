from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request, *args, **kwargs):
   return HttpResponse('OK')

def error404(request, *args, **kwargs):
   return HttpResponse('404 Not Found', status=404, )
