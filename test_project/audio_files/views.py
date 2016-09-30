from django.views.generic.edit import CreateView
from audio_recorder.views import AudioFileCreateViewMixin
from .models import AudioFile
from .forms import AudioFileForm


class AudioFileAPICreateView(AudioFileCreateViewMixin):
    model = AudioFile


class AudioFileCRUDCreateView(CreateView):
    model = AudioFile
    form_class = AudioFileForm
