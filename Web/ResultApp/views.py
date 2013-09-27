#from django.http import HttpResponse 
from ResultApp.models import ResultsList
from django.shortcuts import render
# Create your views here.
def Index(request):
    return render(request, 'ResultApp/index.html')

def LeftMenu(request):
    return render(request, 'ResultApp/menu.html')

def Context(request):
    query_type= request.GET.get('query_option')
    query = request.GET.get('q','')
    if query:
        if query_type == "query_id":
            results = ResultsList.objects.filter(ResultsID__contains=query)
        elif query_type =="query_os":
            results=  ResultsList.objects.filter(OS__contains=query)
    else:
        results = ResultsList.objects.all()
    return render(request, 'ResultApp/context.html',results)
