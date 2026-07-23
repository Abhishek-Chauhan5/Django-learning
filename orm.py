from django.db import models

class Student(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    
    # for getting all data
    
    student = Student.object.all()