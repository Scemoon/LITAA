from django.db import models

# Create your models here.
class ResultsList(models.Model):
    tools = (('LH','lmbench'),('UH','unixbench'),('SM','stream'))
    archtype = (('x86','X86'),('x64','X64'))
    ResultsID=models.AutoField(primary_key=True)
    TestTool=models.CharField(max_length=10,choices=tools)
    Testarch=models.CharField(max_length=10,choices=archtype)
    OS=models.CharField(max_length=20)
    Tester=models.CharField(max_length=20,blank=True)
    TestTime=models.DateField()
    def __unicode__(self):
        return self.Testarch
    
class Lmbench(models.Model):
    resultID=models.ForeignKey(ResultsList)
     
    
    def __unicode__(self):
        return self.TestTool
