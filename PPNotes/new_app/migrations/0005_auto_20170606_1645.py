# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0004_auto_20170605_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seqe',
            name='expre',
            field=models.CharField(max_length=500),
        ),
    ]
