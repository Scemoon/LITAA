from django.contrib import admin
from ResultApp.models import ResultsList
class ResultsAdmin(admin.ModelAdmin):
    pass
admin.site.register(ResultsList, ResultsAdmin)
