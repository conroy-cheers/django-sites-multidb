# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-15 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites_multidb', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dbconfig',
            options={'verbose_name': 'Database configuration', 'verbose_name_plural': 'Database configurations'},
        ),
        migrations.AlterField(
            model_name='dbconfig',
            name='engine',
            field=models.CharField(choices=[('django.db.backends.postgresql', 'PostgreSQL'), ('django.db.backends.mysql', 'MySQL'), ('django.db.backends.sqlite3', 'SQLite'), ('django.db.backends.oracle', 'Oracle')], max_length=100),
        ),
        migrations.AlterField(
            model_name='dbconfig',
            name='host',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dbconfig',
            name='port',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
