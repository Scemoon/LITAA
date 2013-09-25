from django.db import models

# Create your models here.
class ResultsList(models.Model):
    tools = ('lmbench','unixbench','stream')
    ResultsID=models.AutoField(primary_key=True,unique=True)
    TestTool=models.CharField(max_length=2,choices=tools)
    TestTime=models.DateField("TestDate")
    def __unicode__(self):
        return self.TestTool
