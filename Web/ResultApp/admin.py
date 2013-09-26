from django.contrib import admin
from ResultApp.models import ResultsList
class ResultsAdmin(admin.ModelAdmin):
    fields=['TestTool','Testarch','OS','Tester','TestTime']
admin.site.register(ResultsList, ResultsAdmin)
