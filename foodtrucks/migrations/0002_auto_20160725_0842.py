# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtrucks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodtruck',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='foodtruck',
            name='block',
        ),
        migrations.RemoveField(
            model_name='foodtruck',
            name='blocklot',
        ),
        migrations.RemoveField(
            model_name='foodtruck',
            name='cnn',
        ),
        migrations.RemoveField(
            model_name='foodtruck',
            name='expirationdate',
        ),
        migrations.RemoveField(
            model_name='foodtruck',
            name='locationdescription',
        ),
        migrations.RemoveField(
            model_name='foodtruck',
            name='lot',
        ),
        migrations.RemoveField(
            model_name='foodtruck',
            name='noisent',
        ),
        migrations.RemoveField(
            model_name='foodtruck',
            name='permit',
        ),
        migrations.RemoveField(
            model_name='foodtruck',
            name='priorpermit',
        ),
        migrations.RemoveField(
            model_name='foodtruck',
            name='received',
        ),
        migrations.RemoveField(
            model_name='foodtruck',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='foodtruck',
            name='status',
        ),
        migrations.RemoveField(
            model_name='foodtruck',
            name='x',
        ),
        migrations.RemoveField(
            model_name='foodtruck',
            name='y',
        ),
    ]
