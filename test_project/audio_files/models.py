from django.db import models
from audio_recorder import AudioFileMixin


class AudioFile(AudioFileMixin, models.Model):
    pass
