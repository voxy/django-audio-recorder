import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from .views import AudioRecorderAPICreateView
from .models import AudioFile

@pytest.mark.django_db
def test_create_view_mixin(rf):
    request = rf.post('/audio-files/')
    request.FILES['audio_file'] = SimpleUploadedFile("file.txt", "file_content")
    response = AudioRecorderAPICreateView.as_view()(request)
    assert response.status_code == 201
    assert AudioFile.objects.count() == 1