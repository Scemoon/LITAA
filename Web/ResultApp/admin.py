from django.contrib import admin
from ResultApp.models import ResultsList,TestTools,Arch,Lmbench
class ResultsAdmin(admin.ModelAdmin):
    fields=['TestTool','Testarch','HWManufactures','CPU','Memory','OS','Tester','TestTime','Other']
    search_fields = ('OS',)
    list_display = ('ResultsID', 'TestTool','OS', 'TestTime')
    list_filter = ('OS', 'TestTime')
    ordering = ('-ResultsID',)
class LmbenchAdmin(admin.ModelAdmin):
    fields=['ResultsID','TestTimes']
    list_display=('id','ResultsID','TestTimes')
admin.site.register(ResultsList, ResultsAdmin)
admin.site.register(TestTools)
admin.site.register(Arch)
admin.site.register(Lmbench,LmbenchAdmin)

