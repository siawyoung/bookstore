# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
