# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=1, to='dp.Author'),
            preserve_default=False,
        ),
    ]
