from django.db import models

# Create your models here.
# 1st table
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

# 2nd table
class Profile(models.Model):
    bio = models.TextField()
    location = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.location)