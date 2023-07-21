from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Employee(models.Model):
    sno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30,null=False)
    city=models.CharField(max_length=30,null=False)
    
    def __str__(self):
        return self.name