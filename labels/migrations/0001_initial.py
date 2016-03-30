# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-30 01:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_auto_20160330_0058'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('count', models.PositiveIntegerField()),
                ('cultivar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cultivar')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NurseryLabelOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='labelentry',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labels.NurseryLabelOrder'),
        ),
        migrations.AddField(
            model_name='labelentry',
            name='rootstock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Rootstock'),
        ),
    ]
