# Django Audio Recorder

Create a javascript audio recorder and save audio files using django.

## Installation

```
# Install the latest version with
pip install django-audio-recorder
```

## Quickstart

Add `audio_recorder` to your installed apps in your django settings
```python
INSTALLED_APPS = [
    ...
    audio_recorder,
    ...
]
```

Create your model to store the audio file using a [FileField](https://docs.djangoproject.com/en/1.10/ref/models/fields/#filefield). 
```python
from django.db import models
from audio_recorder.models import AudioFileMixin

class AudioFile(AudioFileMixin, models.Model):
    pass
```

Create an audio recorder view using the `AudioRecorderCreateViewMixin`
```python
from audio_recorder.views import AudioFileCreateViewMixin

class AudioFileCreateView(AudioFileCreateViewMixin):
    model = AudioFile
```

Register the view in your urls
```python
urlpatterns = [
    url(r'audio-files/', AudioFileCreateView.as_view(create_field='audio_file'), name='audio-file-create')
]
```

Create a form and use the `AudioFileWidget` for the audio recorder
```python
from django import forms
from audio_recorder.widgets import AudioFileWidget

class AudioFileForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        widgets = {
            'audio_file': AudioFileWidget(url='audio-file-create'),
        }
```

## Development

Setup the environment
```bash
git clone https://github.com/voxy/django-audio-recorder.git
cd django-audio-recorder/test_project
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the development server
```bash
make serve
```

Run lint & tests
```bash
make lint && make tests
```
