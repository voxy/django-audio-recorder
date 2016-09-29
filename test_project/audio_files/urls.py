from django.conf.urls import url
from .views import AudioFileAPICreateView, AudioFileCRUDCreateView

urlpatterns = [
    url(r'^audio-files/$',
        AudioFileAPICreateView.as_view(),
        name='audio-file-api-create'),
    url(r'^audio-files/new$',
        AudioFileCRUDCreateView.as_view(),
        name='audio-file-crud-create')
]
