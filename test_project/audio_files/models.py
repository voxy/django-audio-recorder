from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models


class AudioFile(models.Model):
    audio_file = models.FileField(
        storage=FileSystemStorage(location=settings.MEDIA_ROOT)
    )
