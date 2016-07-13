# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeyValueStore',
            fields=[
                ('keyid', models.TextField(serialize=False, primary_key=True)),
                ('val', models.BinaryField(null=True, blank=True)),
                ('modified', models.DateTimeField(primary_key=True)),
            ],
            options={
                'db_table': 'key_value_store',
                'managed': False,
            },
        ),
    ]
