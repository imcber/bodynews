# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=140)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('cuerpo', models.TextField()),
                ('publicado', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
