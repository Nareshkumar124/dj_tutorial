from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=100,null=False)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.emp_name}"
    
    

    
    

