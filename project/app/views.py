from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from app.models import *
from datetime import date
from datetime import datetime
from datetime import date
import time
# from .task import add
from celery import shared_task
from celery.utils.log import get_logger
# clogger = get_logger(__name__)

from project.logfun import logger  


# function to test Celery
@shared_task
def add(x, y):
    try:
        print(f"----ADD LOG---")
        # logger.info(f"---Storing log to logfile")
        # clogger.info(f"-- celery log --")
        return x + y
    except Exception as e:
        print(f"----Print Error : {str(e)}---")
        # logger.info(f"---error log to logfile : {str(e)} ---")
        # clogger.info(f"-- error celery log : {str(e)}--")
        
# add(2,3)

# testcelery()


@shared_task
def send_event_mail():
    try:
        objs = event_details.objects.filter(date=date.today())
        if not len(objs):
            logger.info(f"No Events Found")
            return True
        for i in objs:
            # send email
            subject = f"{i.event_name}"
            message = f"{i.template_id.template}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [i.user_id.email, ]
            send_mail( subject, message, email_from, recipient_list )
            logger.info(f"Email Sent To : {i.user_id.email}")
            logger.info(f"* * * * * * * * automated mail sent to {i.user_id.email}  at {datetime.now()} * * * * * * * * * * *")
            return True

    except Exception as e:
        logger.info(f"Exception : {str(e)}")
        return False

@api_view(['POST'])
def testcelery(request):
    try:
        # add.delay(2, 3) 
        result = send_event_mail.apply_async(retry=True, retry_policy={'max_retries': 3})
        # time.sleep(10)
        # result.get(timeout=1)
        logger.info(f"RESULT :=> {result.ready(), result.traceback}")
        return Response({"status":f"{result.ready()}"}, status=status.HTTP_200_OK)
    except Exception as e:
        print(f"----Print Error : {str(e)}---")
        return Response({"status":"Failed", "error":f"{str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""# Automatic mail using scheduler
import schedule
import time
  
def func():
    print("Geeksforgeeks")
  
schedule.every(1).minutes.do(send_event_mail)
# schedule.every(5).seconds.do(func)

  
while True:
    print("Check")
    schedule.run_pending()
    time.sleep(60)"""

# celery -A project worker -l INFO & -D -f celery.log