from django.db import models

# Create your models here.
#class TestTools(models.Model):
#    ToolsName = models.CharField(max_length=20)
#    ToolsDesc = models.TextField(blank=True)
    
#    def __unicode__(self):
#        return self.ToolsName
#class Arch(models.Model):
#    HWArch = models.CharField(max_length=20)
    
#    def __unicode__(self):
#        return self.HWArch
   
class ResultsList(models.Model):
    toolslist=(('lmbench','lmbench'),
               ('unixbench','unixbench'),
               ('stream','stream'))
    archlist=(('x86','X86'),
              ('x64','X64'),
              ('mips','mips'))
    ResultsID=models.AutoField(primary_key=True)
    TestTool=models.CharField(max_length=20,choices=toolslist)
    Testarch=models.CharField(max_length=20,choices=archlist)
    HWManufactures=models.CharField(max_length=100,blank=True)
    CPU=models.CharField(max_length=100)
    Memory=models.CharField(max_length=100)
    OS=models.CharField(max_length=100)
    Tester=models.CharField(max_length=20,blank=True)
    TestTime=models.DateField()
    ResultFile=models.FileField(upload_to='%Y%m%d')
    Other=models.TextField(blank=True)
    
    
class Lmbench(models.Model):
    ResultsID=models.OneToOneField(ResultsList)
    TestTimes=models.IntegerField()
    