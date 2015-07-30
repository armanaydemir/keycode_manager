# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userKeyGen', '0012_auto_20150629_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2015, 8, 1, 15, 13, 20, 899038, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='invoice_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 2, 15, 13, 20, 899110, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='keycodes_expire',
            field=models.DateField(default=datetime.datetime(2015, 10, 30, 15, 13, 20, 899134, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='paid_date',
            field=models.DateField(default=datetime.datetime(2015, 8, 1, 15, 13, 20, 899184, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 30, 15, 13, 20, 899945, tzinfo=utc)),
        ),
    ]
