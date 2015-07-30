# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userKeyGen', '0007_auto_20150623_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 23, 18, 32, 9, 360526, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='invoice_date',
            field=models.DateField(default=datetime.datetime(2015, 6, 23, 18, 32, 9, 360586, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='keycodes_expire',
            field=models.DateField(default=datetime.datetime(2015, 10, 21, 18, 32, 9, 360715, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='paid_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 23, 18, 32, 9, 360665, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 21, 18, 32, 9, 361718, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default=models.ForeignKey(to='userKeyGen.Customer'), max_length=64),
        ),
    ]
