# from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from django.contrib.auth import login,logout, authenticate
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.decorators import api_view
# from rest_framework.response import Response
from app.models import *
from datetime import date
# from .seed import seed_data
from datetime import datetime
# seed_data()
from datetime import date
# from .task import add
from celery import shared_task
from celery.utils.log import get_logger
clogger = get_logger(__name__)

# from project.logfun import logger  


# function to test Celery
@shared_task
def add(x, y):
    clogger.info(f"------------------------add function : shared task info--------{x+y}")
    return x + y


@shared_task
def send_event_mail():
    try:
        # print("Check todays event")
        objs = event_details.objects.filter(date=date.today())
        clogger.info(f"No of todays events : {len(objs)}")
        for i in objs:
            # print("EVENT DETAILS : ",i.event_name, i.user_id.email, i.template_id)
            # print("USER DETAILS : ", i.user_id.username, i.user_id.email)
            # print("Template : ",i.template_id.template)

            # send email
            subject = f"{i.event_name}"
            message = f"{i.template_id.template}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [i.user_id.email, ]
            send_mail( subject, message, email_from, recipient_list )
            clogger.info(f"Email Sent To : {i.user_id.email}")
            clogger.info(f"* * * * * * * * automated mail sent to {i.user_id.email}  at {datetime.now()} * * * * * * * * * * *")

        # pass
    except Exception as e:
        clogger.error(f"Exception : {str(e)}")

"""def background_proc():
    # send_event_mail.apply_async( countdown=180,retry_policy={'max_retries': 3}) 
    send_event_mail.apply_async( countdown=10) 

background_proc()
"""

# call shared task in function (background)
def celery_check():
    # run the task in 5 seconds
    
    try:
        # add.delay(2, 2)
        # data = send_event_mail.apply_async(countdown=10)
        # print("# # # # # data # # # ",data)
        result = add.apply_async((2, 3), countdown=10) 
        clogger.info(f"# # # # # # # RESULT :{result, datetime.now()}")#retry_policy={'max_retries': 3}
        # clogger.info(f"# # # # # data # # # {data}")
        clogger.info(f"# # # # # # # RESULT : {result.get(), datetime.now()}")
        
    except Exception as exc:
        clogger.exception('-----------------------------Sending task raised: %r', exc)
        clogger.error('-----------------------------Sending task raised: %r', exc)

celery_check()

