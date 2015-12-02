# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [(b'bookstore_app', '0001_initial'), (b'bookstore_app', '0002_auto_20151130_1804')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(max_length=14, serialize=False, primary_key=True)),
                ('authors', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('year_op', models.DateTimeField(verbose_name=b'year of purchase')),
                ('copies', models.IntegerField(verbose_name=b'available copies')),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('b_format', models.CharField(max_length=2, choices=[(b'hc', b'hardcover'), (b'sc', b'softcover')])),
                ('keywords', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('login_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=40)),
                ('cc_num', models.CharField(max_length=16, verbose_name=b'credit card number')),
                ('address', models.CharField(max_length=100)),
                ('phone_num', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('date_time', models.DateTimeField(verbose_name=b'date time of feedback')),
                ('short_text', models.CharField(max_length=140)),
                ('book', models.ForeignKey(to='bookstore_app.Book')),
                ('rater', models.ForeignKey(to='bookstore_app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField(verbose_name=b'date time of order')),
                ('status', models.CharField(max_length=2, choices=[(b'it', b'in transit to customer'), (b'pp', b'processing payment'), (b'dc', b'delivered to customer'), (b'wh', b'in warehouse')])),
                ('customer', models.ForeignKey(to='bookstore_app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order_book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('copies', models.IntegerField(verbose_name=b'copies ordered')),
                ('book', models.ForeignKey(to='bookstore_app.Book')),
                ('order', models.ForeignKey(to='bookstore_app.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2)])),
                ('book', models.ForeignKey(to='bookstore_app.Book')),
                ('ratee', models.ForeignKey(related_name='ratee', to='bookstore_app.Customer')),
                ('rater', models.ForeignKey(related_name='rater', to='bookstore_app.Customer')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([('book', 'rater', 'ratee')]),
        ),
        migrations.AlterUniqueTogether(
            name='order_book',
            unique_together=set([('order', 'book')]),
        ),
        migrations.AlterUniqueTogether(
            name='feedback',
            unique_together=set([('rater', 'book')]),
        )
    ]
