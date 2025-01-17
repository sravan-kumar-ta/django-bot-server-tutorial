# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2023-02-04 03:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_db', '0005_auto_20230204_0122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('joke1', models.TextField()),
                ('joke2', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='botcall',
            name='dump',
        ),
        migrations.RemoveField(
            model_name='botcall',
            name='fat',
        ),
        migrations.RemoveField(
            model_name='botcall',
            name='stupid',
        ),
        migrations.AddField(
            model_name='botcall',
            name='calls',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='botcall',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='botcall',
            name='bot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chat_db.Bot'),
            preserve_default=False,
        ),
    ]
