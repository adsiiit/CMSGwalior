# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0003_auto_20151023_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofiles',
            name='age',
        ),
        migrations.RemoveField(
            model_name='userprofiles',
            name='gender',
        ),
    ]
