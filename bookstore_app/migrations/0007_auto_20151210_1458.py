# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import datetime

def insert_order(apps, schema_editor):
	Customer = apps.get_model("bookstore_app", "Customer")
	Order = apps.get_model("bookstore_app", "Order")
	raw_data=[['ruso61440','it']
	,['oman2483','pp']
	,['hris79','dc']
	,['ardy46329','wh']
	,['ardy46329','it']
	,['hris79','pp']
	,['oman2483','wh']
	,['oman2483','it']
	,['ruso61440','wh']
	,['ruso61440','pp']]

	for ordervalues in raw_data:
		useri = Order(date_time=str(datetime.datetime.now()), customer = Customer.objects.get(login_id=ordervalues[0]), status = ordervalues[1])
		useri.save()

def insert_order_book(apps, schema_editor):
	Book = apps.get_model("bookstore_app", "Book")
	Order = apps.get_model("bookstore_app", "Order")
	Order_book = apps.get_model("bookstore_app", "Order_book")
	raw_data=[['978-1477468524', 2]
	,['978-1936976027', 1]
	,['978-1461002505',2]
	,['978-0833030474',2]
	,['978-1623366322',4]
	,['978-0345542960',2]
	,['978-0316200608',1]
	,['978-0743200400',1]
	,['978-0060555665',2]
	,['978-0399175527',1]]

	for i in range(len(raw_data)):
		useri = Order_book(order= Order.objects.get(id=i+1), book = Book.objects.get(isbn=raw_data[i][0]), copies = raw_data[i][1])
		useri.save()

class Migration(migrations.Migration):

    dependencies = [
    	('bookstore_app', '0004_auto_20151202_2036'),
    ]

    operations = [
    	migrations.RunPython(insert_order),
    	migrations.RunPython(insert_order_book)
    ]
