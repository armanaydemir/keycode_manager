# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userKeyGen', '0009_auto_20150623_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 23, 20, 7, 33, 529517, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='invoice_date',
            field=models.DateField(default=datetime.datetime(2015, 6, 23, 20, 7, 33, 529569, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='keycodes_expire',
            field=models.DateField(default=datetime.datetime(2015, 10, 21, 20, 7, 33, 529682, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='paid_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 23, 20, 7, 33, 529638, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 21, 20, 7, 33, 530458, tzinfo=utc)),
        ),
    ]
