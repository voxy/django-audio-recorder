from django.forms import ModelForm
from .models import AudioFile
from audio_recorder.widgets import AudioFileWidget


class AudioFileForm(ModelForm):

    class Meta:
        fields = ['audio_file', ]
        model = AudioFile
        widgets = {
            'audio_file': AudioFileWidget(url='audio-file-api-create'),
        }
