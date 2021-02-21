from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getCourse", views.getInput, name="getInput"), #url to page to get the course input
    path("user", views.user, name="user"),              #url to page to user
    path("input", views.takeInput, name="takeInput"),   #url to the page to get input the feedback
    path("mail", views.email, name="email"),            #url to the page to send mail
    path("send", views.send, name="send"),              #url to the page after mail has sent (with mail status)
]
