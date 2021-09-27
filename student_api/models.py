import uuid

from autoslug import AutoSlugField
from django.db import models


class ClassRoom(models.Model):
    """Model definition for ClassRoom."""

    CLASS_CHOICES = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
        ('5', 'Fifth'),
        ('6', 'Sixth'),
        ('7', 'Seventh'),
        ('8', 'Eighth'),
        ('9', 'Ninth'),
        ('10', '10th'),
        ('11', '11th'),
        ('12', '12th'),
    )

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    slug = AutoSlugField(populate_from='name', unique=True)
    name = models.CharField(max_length=200, unique=True, choices=CLASS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for ClassRoom."""

        verbose_name = 'ClassRoom'
        verbose_name_plural = 'ClassRooms'
        ordering = ('name',)

    def __str__(self):
        """Unicode representation of ClassRoom."""
        return self.name


class Teacher(models.Model):
    """Model definition for Teacher."""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )

    slug = AutoSlugField(populate_from='name', unique=True)
    name = models.CharField(max_length=200, unique=True)
    currentClass = models.OneToOneField(
        ClassRoom, on_delete=models.CASCADE, related_name='teacher'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Teacher."""

        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ('created',)

    def __str__(self):
        """Unicode representation of Teacher."""
        return self.name


class Student(models.Model):
    """Model definition for Student."""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    slug = AutoSlugField(populate_from='name', unique=True)
    name = models.CharField(max_length=200)
    roll_no = models.IntegerField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    currentClass = models.ForeignKey(
        ClassRoom, on_delete=models.CASCADE, related_name="students"
    )
    ordering = ('roll_no',)

    class Meta:
        """Meta definition for Student."""

        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ('name',)

    def __str__(self):
        """Unicode representation of Student."""
        return self.name


class Subject(models.Model):
    """Model definition for Subject."""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    slug = AutoSlugField(populate_from='name', unique=True)
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.DO_NOTHING, related_name='subjects'
    )
    students = models.ManyToManyField(Student, related_name='subjects')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Subject."""

        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
        ordering = ('name',)

    def __str__(self):
        """Unicode representation of Subject."""
        return self.name
