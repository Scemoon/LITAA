from django.db import models

# Create your models here.
class ResultsList(models.Model):
    TestID=models.IntegerField()
    TestTool=models.CharField(max_length=200)
    TestTime=models.DateField("TestDate")
    def __unicode__(self):
        return self.TestTool
