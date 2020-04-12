from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Create your models here.
class Class(models.Model):
    GRADE_CHOICES = [
        ('A+', 'A+'),
        ('A', 'A'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('B-', 'B-'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('C-', 'C-'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('D-', 'D-'),
        ('F', 'F'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_class')
    class_name = models.CharField(max_length=50, null=False)
    point_goal = models.CharField(max_length=2, choices=GRADE_CHOICES, default="A")
    actual_points = models.PositiveIntegerField(default=0)
    total_points = models.PositiveIntegerField(default=0, null=False)

    created_date = models.DateTimeField( default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.class_name

class Assignment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_assignment')
    assignment_name = models.CharField(max_length=50, null=False)
    max_points = models.PositiveIntegerField(default=0, null=False)
    earned_points = models.PositiveIntegerField(default=0)
    due_date = models.DateTimeField(default=timezone.now)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

    created_date = models.DateTimeField( default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)
    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.assignment_name