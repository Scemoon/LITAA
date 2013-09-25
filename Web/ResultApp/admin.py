from django.contrib import admin
from ResultApp.models import ResultsList
class ResultsAdmin(admin.ModelAdmin):
    fields = ['TestID', 'TestTool','TestTime']
admin.site.register(ResultsList, ResultsAdmin)
