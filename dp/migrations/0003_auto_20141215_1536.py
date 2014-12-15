# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp', '0002_auto_20141215_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='author',
            name='title',
        ),
    ]
