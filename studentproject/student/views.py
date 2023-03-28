from django.shortcuts import render
from rest_framework import viewsets
from student.models import studentMarksMainModel,StudentMainModel,StudentMarksModel
from student.serializers import StudentMarksMainModelserializer,StudentMainModelserializer,StudentMarksModelserializer

# Create your views here.
class StudentMainModelview(viewsets.ModelViewSet):
    queryset = StudentMainModel.objects.all()
    serializer_class = StudentMainModelserializer

class StudentMarksModelview(viewsets.ModelViewSet):
    queryset = StudentMarksModel.objects.all()
    serializer_class = StudentMarksModelserializer

class StudentMarksMainModelview(viewsets.ModelViewSet):
    queryset = studentMarksMainModel.objects.all()
    serializer_class = StudentMarksMainModelserializer
