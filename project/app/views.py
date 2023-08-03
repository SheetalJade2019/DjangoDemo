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
from datetime import datetime
# seed_data()
from datetime import date
# from .task import add
from celery import shared_task
  
  
@shared_task
def add(x, y):
    return x + y


@api_view(['GET', 'POST'])
def send_event_email(request):
    pass

#1 check event_details table for event
def check_event():
    print("check_event() called")
    objs = event_details.objects.filter(date=date.today())
    print("No of todays events : ",len(objs))
    for i in objs:
        print("EVENT DETAILS : ",i.event_name, i.user_id.email, i.template_id)
        # get email id of bday person
        print("USER DETAILS : ", i.user_id.username, i.user_id.email)
        # get template
        print("Template : ",i.template_id.template)
        # event_template.objects.get(template_id=)
        # send email
        subject = f"{i.event_name}"
        message = f"{i.template_id.template}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [i.user_id.email, ]
        send_mail( subject, message, email_from, recipient_list )
        print(f"Email Sent To : {i.user_id.email}")
    # pass

#2 draft mail by referring template
def draft_mail():
    # run the task in 5 seconds
    result = add.apply_async((2, 3), countdown=60) 
    print("# # # # # # # RESULT :",result, datetime.now())
    
draft_mail()

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
# check_event()
