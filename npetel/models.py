from django.db import models

# Create your models here.
# table for course model
class CourseModel(models.Model):
    courseCode = models.CharField(max_length=20)
    courseName = models.CharField(max_length=100)


# table for learner model
class LearnerModel(models.Model):
    userID = models.IntegerField()
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, default=None)
    classHr = models.IntegerField()
    NoofQuery = models.IntegerField()
    ResponseTime = models.IntegerField()
    SubmissionDate = models.IntegerField()
