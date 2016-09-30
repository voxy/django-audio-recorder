from django.core.files.storage import FileSystemStorage
from django.db import models
from django.conf import settings


class AudioFileMixin(models.Model):
    audio_file = models.FileField(
        storage=FileSystemStorage(location=settings.MEDIA_ROOT)
    )

    class Meta:
        abstract = True
