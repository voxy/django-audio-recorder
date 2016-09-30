import time

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse
from splinter import Browser

from .views import AudioFileAPICreateView
from .models import AudioFile


@pytest.mark.django_db
def test_audio_file_api_create_view(rf):
    request = rf.post('/audio-files/')
    request.FILES['audio_file'] = SimpleUploadedFile(
        "file.txt", "file_content"
    )
    response = AudioFileAPICreateView.as_view(create_field='audio_file')(request)  # nopep8
    assert response.status_code == 201
    assert AudioFile.objects.count() == 1


@pytest.mark.live_server
def test_audio_file_crud_create_view(live_server):
    profile_preferences = {'media.navigator.permission.disabled': True}
    with Browser('firefox', profile_preferences=profile_preferences) as browser:  # nopep8
        browser.visit(live_server.url + reverse('audio-file-crud-create'))

        # Wait for the js to load
        time.sleep(2)

        record_button = browser.find_by_id("js-record-button").first
        assert record_button['disabled'] is None

        stop_button = browser.find_by_id("js-stop-button").first
        assert stop_button['disabled'] == 'true'

        audio_element = browser.find_by_id("js-audio").first
        assert audio_element.visible
        assert audio_element['src'] == ''

        record_button.click()
        assert stop_button['disabled'] is None
        assert record_button['disabled'] == 'true'

        stop_button.click()

        assert record_button['disabled'] is None
        assert stop_button['disabled'] == 'true'
        assert audio_element['src'] is not None
