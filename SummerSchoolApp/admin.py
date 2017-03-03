from django.contrib import admin
from .models import *


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year']


class ImportantDateAdmin(admin.ModelAdmin):
    list_display = ['id', 'academic_schedule', 'date']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_type', 'course_no', 'course_title', 'professor']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'title', 'year']

# Register your models here.
admin.site.register(Review, ReviewAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(ReviewImage)
admin.site.register(Course, CourseAdmin)
admin.site.register(ImportantDate, ImportantDateAdmin)
admin.site.register(QuestionAndAnswer)
