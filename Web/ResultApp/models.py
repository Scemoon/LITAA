from django.db import models

# Create your models here.
class ResultsList(models.Model):
    tools = (('LH','lmbench'),('UH','unixbench'),('SM','stream'))
    archtype = (('x86','X86'),('x64','X64'))
    ResultsID=models.AutoField(primary_key=True)
    TestTool=models.CharField(max_length=2,choices=tools)
    Arch=models.CharField(max_length=3,choices=archtype)
    OS=models.CharField(max_length=20)
    Tester=models.CharField(max_length=20)
    TestTime=models.DateField("TestDate")
    
class Lmbench(models.Model):
    pass
    
    def __unicode__(self):
        return self.TestTool
