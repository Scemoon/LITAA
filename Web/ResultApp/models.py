from django.db import models

# Create your models here.
class TestTools(models.Model):
    ToolsName = models.CharField(max_length=20,unique=True)
    ToolsDesc = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.ToolsName
class Arch(models.Model):
    HWArch = models.CharField(max_length=20,unique=True)
    
    def __unicode__(self):
        return self.HWArch
    
class ResultsList(models.Model):
    ResultsID=models.AutoField(primary_key=True)
    TestTool=models.ForeignKey(TestTools)
    Testarch=models.ForeignKey(Arch)
    HWManufactures=models.CharField(max_length=100,blank=True)
    CPU=models.CharField(max_length=100)
    Memory=models.CharField(max_length=100)
    OS=models.CharField(max_length=100)
    Tester=models.CharField(max_length=20,blank=True)
    TestTime=models.DateField()
    Other=models.TextField(blank=True)
    
    
class Lmbench(models.Model):
    ResultsID=models.OneToOneField(ResultsList,related_name='ResultsList_set')
    TestTimes=models.IntegerField()
    