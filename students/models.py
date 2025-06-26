from django.db import models

# Create your models here.
class Student(models.Model):

    student_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100,null=False,blank=False)
    branch = models.CharField(max_length=100,null=False,blank=False)


    def __str__(self):
        return self.name