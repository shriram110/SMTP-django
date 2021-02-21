from django.contrib import admin
from .models import CourseModel, LearnerModel

# Register your models here.
admin.site.register(CourseModel)
admin.site.register(LearnerModel)
