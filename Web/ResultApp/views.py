from django.db.models import Q
from ResultApp.models import ResultsList
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

#create page
class CreatePaginator(Paginator):
    def __init__(self, object_list, per_page, range_num=5, orphans=0, allow_empty_first_page=True):
        Paginator.__init__(self, object_list, per_page, orphans, allow_empty_first_page)
        self.range_num = range_num
  
    def page(self, number):
        self.page_num = number
        return super(CreatePaginator, self).page(number)
 
    def _page_range_ext(self):
        num_count = 2 * self.range_num + 1
        if self.num_pages <= num_count:
            return range(1, self.num_pages + 1)
        num_list = []
        num_list.append(self.page_num)
        for i in range(1, self.range_num + 1):
            if self.page_num - i <= 0:
                num_list.append(num_count + self.page_num - i)
            else:
                num_list.append(self.page_num - i)
 
            if self.page_num + i <= self.num_pages:
                num_list.append(self.page_num + i)
            else:
                num_list.append(self.page_num + i - num_count)
        num_list.sort()
        return num_list
    page_range_ext = property(_page_range_ext)
      

# Create your views here.
def Index(request):
    return render(request, 'ResultApp/index.html')

def LeftMenu(request):
    return render(request, 'ResultApp/menu.html')

def Context(request):
    query = request.GET.get('q','')
    num_pages=request.GET.get('page','1')
    
    if query:
        qset = (
              Q(OS__icontains=query) |
              Q(Tester__icontains=query) |
              Q(TestTool__icontains=query) |
              Q(ResultsID__icontains=query) 
               )
        results =ResultsList.objects.filter(qset)
    else:
        results = ResultsList.objects.all()
        
    results = results.order_by("-ResultsID")
    paginator = CreatePaginator(results,15)
    PageJp = request.GET.get('PageSh','')
    print PageJp
    try:
        if PageJp:
            results=paginator.page(PageJp)
        else:
            results=paginator.page(num_pages)
        
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results =paginator.page(paginator.num_pages)
    return render(request, 'ResultApp/context.html',{"results":results,"query":query,'pages_num':PageJp})
