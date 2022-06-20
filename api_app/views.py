from django.shortcuts import render
from .serializers import StudentSerializer,CourseSerializer
from .models import Student,Course
from rest_framework import viewsets

# Create your views here.

class StudentViewsets(viewsets.ModelViewSet):#capital S
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewsets(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer