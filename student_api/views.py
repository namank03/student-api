from rest_framework import viewsets

from .models import ClassRoom, Student, Subject, Teacher
from .serializers import (
    ClassRoomSerializer,
    StudentSerializer,
    SubjectSerializer,
    TeacherSerializer,
)


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'slug'
    filterset_fields = [
        'name',
    ]


# Create your views here.
class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    lookup_field = 'slug'
    filterset_fields = ['name']


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'slug'
    filterset_fields = ['name', 'subjects']


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = 'slug'
    filterset_fields = ['name', 'teacher']
