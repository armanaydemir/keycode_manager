# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userKeyGen', '0002_auto_20150622_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='bill_amount',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='exchanges',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='keycodes_expire',
            field=models.DateField(default=datetime.datetime(2015, 10, 21, 15, 27, 31, 833378, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='customer',
            name='paid_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 23, 15, 27, 31, 833333, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='customer',
            name='system',
            field=models.CharField(default=b'Edge (hosted)', max_length=64, choices=[(b'Edge (hosted)', b'Edge (hosted)'), (b'Edge (non-hosted)', b'Edge (non-hosted)'), (b'Tradepad', b'Tradepad'), (b'Edge Risk (hosted)', b'Edge Risk (hosted)'), (b'Edge Risk (non-hosted)', b'Edge Risk (non-hosted)')]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 23, 15, 27, 31, 833204, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='invoice_date',
            field=models.DateField(default=datetime.datetime(2015, 6, 23, 15, 27, 31, 833257, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 21, 15, 27, 31, 834195, tzinfo=utc)),
        ),
    ]
