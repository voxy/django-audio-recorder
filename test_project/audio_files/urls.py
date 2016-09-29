from django.conf.urls import url
from .views import AudioRecorderAPICreateView

urlpatterns = [
    url(r'audio-files/', AudioRecorderAPICreateView.as_view())
]
