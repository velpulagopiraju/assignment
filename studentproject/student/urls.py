from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from student.views import StudentMainModelview,StudentMarksModelview,StudentMarksMainModelview

router = routers.DefaultRouter()
router.register(r'studentmainmodel', StudentMainModelview)
router.register(r'studentmarksmodel', StudentMarksModelview)
router.register(r'studentmarksmainmodel',StudentMarksMainModelview )

urlpatterns = [
    path('',include(router.urls)),
]