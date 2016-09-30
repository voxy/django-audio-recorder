# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('audio_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/Users/voxy/workspace/django-audio-recorder/test_project/media'), upload_to=b'')),
            ],
        ),
    ]
