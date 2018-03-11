# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0004_book_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='download',
            field=models.CharField(max_length=50, null=True),
        ),
    ]