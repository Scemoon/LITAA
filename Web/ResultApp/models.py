from django.db import models

# Create your models here.
class ArchList(models.Model):
    ArchName=models.CharField(max_length=20)
    def __str__(self):
        return self.ArchName
   
class TestTool(models.Model):
    ToolName=models.CharField(max_length=20)
    ToolDescription=models.TextField()
    def __str__(self):
        return self.ToolName
   
class ResultsList(models.Model):
    ResultsID=models.AutoField(primary_key=True)
    ToolName=models.ForeignKey(TestTool)
    ArchName=models.ForeignKey(ArchList)
    HWManufactures=models.CharField(max_length=100,blank=True)
    CPU=models.CharField(max_length=100)
    Memory=models.CharField(max_length=100)
    OS=models.CharField(max_length=100)
    Tester=models.CharField(max_length=20,blank=True)
    TestTime=models.DateField()
    ResultFile=models.FileField(upload_to='%Y%m%d')
    Other=models.TextField(blank=True)
 


    