# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('invoice_date', models.DateField(default=datetime.datetime(2015, 6, 22, 20, 19, 37, 593580, tzinfo=utc))),
                ('due_date', models.DateField(default=datetime.datetime(2015, 6, 22, 20, 19, 37, 593623, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('expiration_date', models.DateField(default=datetime.datetime(2015, 10, 20, 20, 19, 37, 594181, tzinfo=utc))),
                ('customer', models.ForeignKey(to='userKeyGen.Customer')),
            ],
        ),
    ]
