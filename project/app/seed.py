from .models import * 
import datetime

def seed_data():
    d = datetime.date(2022, 8, 3)
    try:
        if User.objects.all():
            return 
        su = User.objects.create(username="admin", password="admin", email="admin@mailinator.com",is_superuser=True)
        s = User.objects.create(username="sheetal", password="admin", email="sheetal@mailinator.com")
        p = User.objects.create(username="pranav", password="admin", email="pranav@mailinator.com")

        bt = event_template.objects.create(event_type = "birthday",template=f"Dear name,\nSending you warm birthday wishes and lots of love. May this birthday bring you all the successes you deserve.")
        wat = event_template.objects.create(event_type = "work_anniversery",template=f"Dear name,\nCongratulations on your work anniversary! It’s a special day to celebrate your great work and dedication to your job over the years. We appreciate all that you’ve done and wish you all the best for many more successful years to come!")
        bt = event_template.objects.create(event_type = "alert",template=f"Dear name,\nYour Password Changed")

        # su=User.objects.get(username="admin")
        # ou=User.objects.get(username="SheetalJade")

        # e = event_details.objects.create(event_name=f"Happy Birthday {name}..!!", user_id=s, template_id=bt,date=d)
        # e = event_details.objects.create(event_name=f"Happy Work Anniversary, {name}!", user_id=p, template_id=wat,date=d)

    except Exception as e:
        print("Exception : ",str(e))
"""

Event Name : f"Happy Birthday {name}..!!"
Message : f"Dear name,\nSending you warm birthday wishes and lots of love. May this birthday bring you all the successes you deserve."

Event Name : f"Happy Work Anniversary, {name}!"
Message : f"Dear {name},\nCongratulations on your work anniversary! It’s a special day to celebrate your great work and dedication to your job over the years. We appreciate all that you’ve done and wish you all the best for many more successful years to come!"

Event Name : f"Security Alert!"
Message : f"Dear {name},\n Password Changed"

event_type : birthday
event_type : work_anniversery
event_type : alert 


# Sequence for database seed:
add super user
add other users
add template
add event
"""

