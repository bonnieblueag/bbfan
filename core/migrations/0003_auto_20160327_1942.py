# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-27 19:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160327_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='city',
            new_name='center',
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('center', 'state', 'country')]),
        ),
    ]