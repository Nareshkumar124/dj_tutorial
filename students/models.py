from django.db import models

# Create your models here.
class Student(models.Model):

    student_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100,null=False,blank=False)
    branch = models.CharField(max_length=100,null=False,blank=False)


    def __str__(self):
        return self.name
    
    @classmethod
    def get_student_by_name(cls, name):
        """Retrieve a student by their name."""
        try:
            return cls.objects.get(name=name)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_student_by_id(cls, student_id):
        """Retrieve a student by their ID."""
        try:
            return cls.objects.get(student_id=student_id)
        except cls.DoesNotExist:
            return None
        
    def update_single_student(self,data):
        self.name = data['name']
        self.branch = data['branch']
        self.save()
        return self
        
        
    
    
    
    
