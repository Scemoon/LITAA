from django.db.models import Q
from ResultApp.models import ResultsList
from django.shortcuts import render
# Create your views here.
def Index(request):
    return render(request, 'ResultApp/index.html')

def LeftMenu(request):
    return render(request, 'ResultApp/menu.html')

def Context(request):
    query = request.GET.get('q','')
    if query:
        qset = (
              Q(OS__icontains=query) |
              Q(Tester__icontains=query) |
              Q(TestTools__icontains=query) |
              Q(ResutlsID__icontains=query) 
               )
        results =ResultsList.objects.filter(qset)
    else:
        results = ResultsList.objects.all()
        
    print results
    return render(request, 'ResultApp/context.html',results)
