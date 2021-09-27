from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from .models import ClassRoom, Student, Subject, Teacher


class SubjectSerializer(
    FlexFieldsModelSerializer, serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = Subject
        fields = ('url', 'name', 'slug', 'students', 'teacher')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
            'students': {'lookup_field': 'slug'},
            'teacher': {'lookup_field': 'slug'},
        }
        expandable_fields = {
            'students': ('student_api.StudentSerializer', {'many': True}),
            'teacher': ('student_api.TeacherSerializer', {'many': True}),
        }


class StudentSerializer(
    FlexFieldsModelSerializer, serializers.HyperlinkedModelSerializer
):
    # subjects = SubjectSerializer(fields=['name', 'slug', 'id'])

    class Meta:
        model = Student
        fields = ('url', 'name', 'roll_no', 'updated', 'subjects', 'currentClass')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
            'subjects': {'lookup_field': 'slug'},
            'currentClass': {'lookup_field': 'slug'},
        }
        expandable_fields = {
            'subjects': ('student_api.SubjectSerializer', {'many': True}),
            'currentClass': ('student_api.ClassRoomSerializer', {'many': False}),
        }


class TeacherSerializer(
    FlexFieldsModelSerializer, serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = Teacher
        fields = (
            'url',
            'name',
            'currentClass',
            'subjects',
            'slug',
        )
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
            'subjects': {'lookup_field': 'slug'},
            'currentClass': {'lookup_field': 'slug'},
        }
        expandable_fields = {
            'subjects': ('student_api.SubjectSerializer', {'many': True}),
            'currentClass': ('student_api.ClassRoomSerializer'),
        }


class ClassRoomSerializer(
    FlexFieldsModelSerializer, serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = ClassRoom
        fields = ('url', 'name', 'created', 'teacher', 'students')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
            'teacher': {'lookup_field': 'slug', 'read_only': True},
            'students': {'lookup_field': 'slug', 'read_only': True},
        }
        expandable_fields = {
            'teacher': ('student_api.TeacherSerializer'),
            'students': ('student_api.StudentSerializer', {'many': True}),
        }


# from student_api.serializers import (ClassRoomSerializer, StudentSerializer,
#  SubjectSerializer, TeacherSerializer)

# print(repr(s))
