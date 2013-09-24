from django.contrib import admin
from ResultApp import ResultsList
class ResultsAdmin(admin.ModelAdmin):
    fields = ['TestID', 'TestTool','TestTime']

admin.site.register(ResultsList, ResultsAdmin)
