from django.contrib import admin
from ResultApp.models import ResultsList
from ResultApp.models import ArchList,TestTool
class ResultsAdmin(admin.ModelAdmin):
    fields=['ToolName','ArchName','HWManufactures','CPU','Memory','OS','Tester','ResultFile','TestTime','Other']
    search_fields = ('OS','ToolName','HWManufactures')
    list_display = ('ResultsID', 'ToolName','OS', 'TestTime','ResultFile')
    list_filter = ('OS', 'TestTime')
    ordering = ('-ResultsID',)
admin.site.register(ResultsList, ResultsAdmin)
admin.site.register(ArchList)
admin.site.register(TestTool)
