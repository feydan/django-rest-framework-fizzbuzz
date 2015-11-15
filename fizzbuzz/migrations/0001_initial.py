# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FizzBuzz',
            fields=[
                ('fizzbuzz_id', models.AutoField(serialize=False, primary_key=True)),
                ('useragent', models.CharField(default=b'', max_length=256, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(default=b'', max_length=256, blank=True)),
            ],
            options={
                'ordering': ('fizzbuzz_id', 'useragent', 'creation_date', 'message'),
            },
        ),
    ]
