from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    emobile=models.CharField(max_length=60)
    eemail=models.CharField(max_length=40)
    eaddress=models.CharField(max_length=100)
