# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_app', '0003_auto_20151202_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year_op',
            field=models.DateTimeField(verbose_name=b'year of publication'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date time of feedback'),
        ),
    ]
