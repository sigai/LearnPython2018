# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]