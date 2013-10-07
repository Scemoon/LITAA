from django.contrib import admin
from ResultApp.models import ResultsList,Lmbench
class ResultsAdmin(admin.ModelAdmin):
    fields=['TestTool','Testarch','HWManufactures','CPU','Memory','OS','Tester','ResultFile','TestTime','Other']
    search_fields = ('OS','TestTool','HWManufactures')
    list_display = ('ResultsID', 'TestTool','OS', 'TestTime','ResultFile')
    list_filter = ('OS', 'TestTime')
    ordering = ('-ResultsID',)
admin.site.register(ResultsList, ResultsAdmin)


