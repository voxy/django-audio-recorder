from django.core.urlresolvers import reverse
from django.forms import HiddenInput
from django.contrib.staticfiles.templatetags.staticfiles import static


class AudioFileWidget(HiddenInput):

    class Media:
        js = (
            'audio_recorder/recorder.js',
            'audio_recorder/csrf.js',
        )

    def __init__(self, url=None, *args, **kwargs):
        self.url = url
        super(AudioFileWidget, self).__init__(*args, **kwargs)

    def build_attrs(self, *args, **kwargs):
        """Build HTML attributes for the widget."""
        attrs = super(AudioFileWidget, self).build_attrs(*args, **kwargs)
        if self.url is not None:
            attrs['data-url'] = reverse(self.url)
            attrs['data-django-audio-recorder'] = True

        return attrs

    def render(self, name, value, attrs=None):
        html = super(AudioFileWidget, self).render(name, value, attrs=None)
        if value:
            instance = self.choices.queryset.filter(id=value).first()
            audio_template = (
                '<audio id="js-audio" controls>'
                '    <source src={url}>'
                '</audio>'
            ).format(url=instance.audio_file.url)
        else:
            audio_template = (
                '<audio id="js-audio" controls>'
                '    <source>'
                '</audio>'
            )
        return audio_template + (
           '<br />'
           '<div class="btn-group" role="group">'
           '    <button id="js-record-button" '
           '            type="button" class="btn btn-default">'
           '        Record'
           '    </button>'
           '    <button id="js-stop-button" '
           '            type="button" class="btn btn-default" disabled="disabled">'  # nopep8
           '        Stop'
           '    </button>'
           '</div>'
           '<span id="js-upload-span" '
           '      class="hidden">'
           '    Uploading...'
           '</span>'
           '<br />'
           '<br />'
        ) + html
