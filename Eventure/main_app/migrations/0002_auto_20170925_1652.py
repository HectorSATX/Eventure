# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='user',
        ),
        migrations.RemoveField(
            model_name='eventinfo',
            name='host',
        ),
        migrations.AddField(
            model_name='eventinfo',
            name='userProfile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.UserProfile'),
        ),
        migrations.DeleteModel(
            name='Host',
        ),
    ]
