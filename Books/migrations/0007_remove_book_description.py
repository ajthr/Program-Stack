# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-01 15:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0006_auto_20180226_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
    ]
