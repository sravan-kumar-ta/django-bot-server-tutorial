# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2023-02-03 19:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat_db', '0003_auto_20230203_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stupid', models.PositiveIntegerField(default=0)),
                ('fat', models.PositiveIntegerField(default=0)),
                ('dumb', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='message',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
