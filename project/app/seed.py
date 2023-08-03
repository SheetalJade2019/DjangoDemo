from .models import * 
import datetime

def seed_data():
    d = datetime.date(2022, 8, 3)
    try:
        if User.objects.all():
            return 
        su = User.objects.create(username="admin", password="admin", email="admin@gmail.com",is_superuser=True)
        ou = User.objects.create(username="SheetalJade", password="admin", email="sheetal.jade93@gmail.com")
        bt = event_template.objects.create(event_type = "birthday",template="[template] HAPPY BIRTHDAY..!")
        wat = event_template.objects.create(event_type = "work anniversery",template="[template] HAPPY WORK ANNIVERSORY..!")
        su=User.objects.get(username="admin")
        ou=User.objects.get(username="SheetalJade")

        e = event_details.objects.create(event_name="BIRTHDAY", user_id=ou, template_id=bt,date=d)
        e = event_details.objects.create(event_name="WORK ANN", user_id=ou, template_id=wat,date=d)

    except Exception as e:
        print("Exception : ",str(e))