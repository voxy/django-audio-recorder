from __future__ import unicode_literals

from django.db import models

class AudioFile(models.Model):
    audio_file = models.FileField()