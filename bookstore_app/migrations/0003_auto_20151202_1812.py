# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def insert_users(apps, schema_editor):
    Customer = apps.get_model("bookstore_app", "Customer")
    user1 = Customer(login_id="user_1", name="User 1", password="lol", cc_num="12341234", address="Uptown", phone_num="12341234")
    user2 = Customer(login_id="user_2", name="User 2", password="lol", cc_num="12341234", address="Uptown", phone_num="12341234")
    user1.save()
    user2.save()

class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_app', '0002_auto_20151130_1804'),
    ]

    operations = [
        migrations.RunPython(insert_users)
    ]



# # -*- coding: utf-8 -*-
# from django.db import models, migrations

# def combine_names(apps, schema_editor):
#     # We can't import the Person model directly as it may be a newer
#     # version than this migration expects. We use the historical version.
#     Person = apps.get_model("yourappname", "Person")
#     for person in Person.objects.all():
#         person.name = "%s %s" % (person.first_name, person.last_name)
#         person.save()

# class Migration(migrations.Migration):

#     dependencies = [
#         ('yourappname', '0001_initial'),
#     ]

#     operations = [
#         migrations.RunPython(combine_names),
#     ]