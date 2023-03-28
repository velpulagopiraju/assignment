from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from student.models import StudentMainModel,studentMarksMainModel,StudentMarksModel


class StudentMainModelserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentMainModel
        fields = '__all__'
    
class StudentMarksModelserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentMarksModel
        fields = '__all__'

class StudentMarksMainModelserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = studentMarksMainModel
        fields = '__all__'