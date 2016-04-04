from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request, *args, **kwargs):
   return HttpResponse("OK", status =200)

def question (request, *args, **kwargs):
   value = " =) <br>"
   try: 
      for k in kwargs:
         value = value + str(k) + " = " str(kwargs[k]) + "<br>"
   except NameError:
      value = " not key <br>" 
   except IndexError:
      value = "..."
   except BaseException:
      value = "///////"
   else: 
      value = "0000"
   if value == None:
      value = "=("
   value = value + " and "
   if value == None:
      value = "NOOOOOOOOOOOOOOOOOOOOOOO!"
   return HttpResponse(value, status=200)

def error404(request, *args, **kwargs):
   return HttpResponse('404 Not Found', status=404, )
