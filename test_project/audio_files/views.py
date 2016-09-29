from audio_recorder.views import CreateViewMixin
from .models import AudioFile


class AudioRecorderAPICreateView(CreateViewMixin):
    model = AudioFile
