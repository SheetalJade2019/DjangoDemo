from django.db import models
from django.contrib.auth.models import User

EVENT_TYPE_CHOICES = (("birthday","birthday"),("work anniversery","work anniversery"))

class event_template(models.Model):
    template_id = models.AutoField(primary_key=True)
    event_type  = models.CharField(max_length = 30,choices=EVENT_TYPE_CHOICES,default="birthday")
    template = models.TextField()

class event_details(models.Model):
    event_name  = models.CharField(max_length = 200)
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    template_id = models.ForeignKey(event_template, null=True, on_delete=models.CASCADE)
    date = models.DateField()


