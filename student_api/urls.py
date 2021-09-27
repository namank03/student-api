from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ClassRoomViewSet, StudentViewSet, SubjectViewSet, TeacherViewSet

router = DefaultRouter()

router.register('students', StudentViewSet)
router.register('classrooms', ClassRoomViewSet)
router.register('subjects', SubjectViewSet)
router.register('teachers', TeacherViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
