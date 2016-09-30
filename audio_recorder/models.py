from django.db import models


class AudioFileMixin(models.Model):
    audio_file = models.FileField()

    class Meta:
        abstract = True
