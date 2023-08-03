from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import *
from datetime import date
from .seed import seed_data

seed_data()


@api_view(['GET', 'POST'])
def send_event_email(request):
    pass

#1 check event_details table for event
def check_event():
    pass

#2 draft mail by referring template
def draft_mail():
    pass 

#3 send mail
def try_send_mail(subject, message,email_from, recipient_list):
    try:
        # subject = sub#'welcome to Automated Email ..!'
        # message = msg#f'Hi Sheetal, Email sent successfully'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail( subject, message, email_from, recipient_list )
        print("sending mail: Success")

    except Exception as e :
        print("Exception", str(e))   
# try_send_mail()

def add_user(uname, pwd, email):
    try:
        User.objects.create(username=uname, password=pwd, email=email)
    except Exception as e:
        print("Exception while adding user : ", str(e))

def add_event(event_name, user_id, template_id):
    try:
        event_details.objects.create(event_name,user_id=user_id,template_id=template_id, date=date)
    except Exception as e:
        print("Exception while adding event : ", str(e))

def add_template( event_type, template):
    try:
        event_template.objects.create(event_type=event_type, template=template)
    except Exception as e:
        print("Exception while adding template : ", str(e))

# add_user("SJade", "SJade", "sheetal.jade93@gmail.com")
# add_event("BIRTHDAY", 1, 1)
# add_template("birthday","HAPPY BIRTHDAY..!")
