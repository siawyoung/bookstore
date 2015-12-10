# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_app', '0007_auto_20151210_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=2, choices=[(b'it', b'in transit to customer'), (b'pp', b'processing payment'), (b'dc', b'delivered to customer'), (b'wh', b'in warehouse'), (b'ns', b'not submitted')]),
        ),
    ]
