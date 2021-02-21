from django.shortcuts import render
from .models import CourseModel, LearnerModel
from django.http import HttpResponse, HttpResponseRedirect
import smtplib

# Create your views here.
# function to render  home page of our application
def index(request):
    return render(request, "index.html")


# function to get input of course
def getInput(request):
    course_name = request.POST["course_name"]
    course_code = request.POST["course_code"]
    CourseModel(courseCode=course_code, courseName=course_name).save()
    return HttpResponseRedirect("/")


# function to render feedback input page
def user(request):
    return render(request, "feedback.html", {"courses": CourseModel.objects.all()})


# function to get input
def takeInput(request):
    userid = request.POST["userid"]
    coursecode = request.POST["course_code"]
    attendance = int(request.POST["attendance_hrs"])
    queries = int(request.POST["queries"])
    response = int(request.POST["response"])
    submission = int(request.POST["submission"])
    obj = CourseModel.objects.get(courseCode=coursecode)
    LearnerModel(
        userID=userid,
        course=obj,
        classHr=attendance,
        NoofQuery=queries,
        ResponseTime=response,
        SubmissionDate=submission,
    ).save()
    return HttpResponseRedirect("user")


# function to render email page
def email(request):
    return render(request, "email.html", {"courses": CourseModel.objects.all()})


# function to send the email to the client
def send(request):
    client = request.POST["client"]
    userid = int(request.POST["userid"])
    coursecode = request.POST["course_code"]
    obj = CourseModel.objects.get(courseCode=coursecode)
    sender_email = "shrirambharadwajsb@gmail.com"
    password = "shriram*111"
    try:
        user = LearnerModel.objects.get(userID=userid, course=obj)
        total = user.classHr + user.NoofQuery + user.ResponseTime + user.SubmissionDate
        avg = float(total) / 4.0
        msg = obj.courseName + " Average " + str(avg) + " Total " + str(total)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, client, msg)
        flag = 1
    except:
        flag = 0

    return render(
        request,
        "sent.html",
        {"total": total, "average": avg, "course": coursecode, "flag": flag},
    )
