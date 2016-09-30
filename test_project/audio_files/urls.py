from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import AudioFileAPICreateView, AudioFileCRUDCreateView

urlpatterns = [
    url(r'^audio-files/$',
        AudioFileAPICreateView.as_view(create_field='audio_file'),
        name='audio-file-api-create'),
    url(r'^audio-files/new$',
        AudioFileCRUDCreateView.as_view(),
        name='audio-file-crud-create')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
