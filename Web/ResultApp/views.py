#from django.http import HttpResponse 
from django.shortcuts import render
# Create your views here.
def Index(request):
    return render(request, 'ResultApp/index.html')

def LeftMenu(request):
    return render(request, 'ResultApp/menu.html')

def Context(request):
    return render(request, 'ResultApp/context.html')
