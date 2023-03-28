import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class StudentMainModel(models.Model):
    name = models.CharField(max_length=100)
    Dob = models.DateField(default=True)
    gender = models.CharField(max_length=50,choices=(('male','male'),('female','female'),('others','others')))
    

class StudentMarksModel(models.Model):
    student = models.ForeignKey(StudentMainModel,on_delete=models.CASCADE)
    Marks = models.CharField(max_length=50)
    sem = models.CharField(max_length=200,choices=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'))) 


class studentMarksMainModel(models.Model):
    student = models.OneToOneField(StudentMainModel,on_delete=models.CASCADE)
    marks = models.ManyToManyField(StudentMarksModel,default='')
    branch = models.CharField(max_length=100,choices=(('Mech','Mech'),('csc','csc'),('ece','ece'),('it','it'),('civil','civil')))
    
    
   
