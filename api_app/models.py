from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
