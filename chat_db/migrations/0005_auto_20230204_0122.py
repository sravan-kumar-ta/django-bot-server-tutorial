# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2023-02-03 19:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_db', '0004_auto_20230204_0117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='botcall',
            old_name='dumb',
            new_name='dump',
        ),
    ]