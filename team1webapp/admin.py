from django.contrib import admin
from .models import Class, Assignment
# Register your models here.
class ClassList(admin.ModelAdmin):
    list_display = ('class_name', 'point_goal', 'total_points', 'actual_points')
    search_fields = ('class_name',)
    ordering = ['class_name']
    list_filter = ('class_name',)

    def __str__(self):
        return self.class_name

class AssignmentList(admin.ModelAdmin):
    list_display = ('class_name', 'assignment_name', 'due_date', 'max_points', 'earned_points')
    search_fields = ('assignment_name',)
    list_filter = ('class_name', 'assignment_name')
    ordering = ['class_name']

    def __str__(self):
        return self.assignment_name

admin.site.register(Class, ClassList)
admin.site.register(Assignment, AssignmentList)