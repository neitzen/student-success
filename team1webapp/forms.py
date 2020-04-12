from .models import Assignment, Class
from django import forms


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('class_name', 'point_goal', 'total_points', 'actual_points')


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('class_name', 'assignment_name', 'due_date', 'max_points', 'earned_points')