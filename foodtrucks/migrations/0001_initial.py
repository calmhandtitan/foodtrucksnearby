# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foodtruck',
            fields=[
                ('objectid', models.IntegerField(serialize=False, primary_key=True)),
                ('applicant', models.CharField(max_length=128, null=True, blank=True)),
                ('facilitytype', models.CharField(default=b'Truck', max_length=64, null=True, blank=True)),
                ('cnn', models.IntegerField(null=True, blank=True)),
                ('locationdescription', models.CharField(max_length=512, null=True, blank=True)),
                ('address', models.CharField(max_length=512, null=True, blank=True)),
                ('blocklot', models.CharField(max_length=16, null=True, blank=True)),
                ('block', models.CharField(max_length=16, null=True, blank=True)),
                ('lot', models.CharField(max_length=16, null=True, blank=True)),
                ('permit', models.CharField(max_length=16, null=True, blank=True)),
                ('status', models.CharField(max_length=16, null=True, blank=True)),
                ('fooditems', models.CharField(max_length=512, null=True, blank=True)),
                ('x', models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)),
                ('y', models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)),
                ('latitude', models.DecimalField(db_index=True, null=True, max_digits=15, decimal_places=12, blank=True)),
                ('longitude', models.DecimalField(db_index=True, null=True, max_digits=15, decimal_places=12, blank=True)),
                ('schedule', models.URLField(max_length=512, null=True, blank=True)),
                ('noisent', models.DateTimeField(null=True, blank=True)),
                ('approved', models.DateTimeField(null=True, blank=True)),
                ('received', models.DateTimeField(null=True, blank=True)),
                ('priorpermit', models.IntegerField(null=True, blank=True)),
                ('expirationdate', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'ordering': ('objectid',),
            },
            bases=(models.Model,),
        ),
    ]
