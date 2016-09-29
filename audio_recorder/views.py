from django import http
from django.views.generic.base import View


class CreateViewMixin(View):
    model = None

    def post(self, request):
        audio_file = request.FILES.get('audio_file', None)

        if audio_file is None:
            return http.HttpResponseBadRequest()

        result = self.model.objects.create(**{'audio_file': audio_file})

        return http.JsonResponse({
            'id': result.pk,
            'url': result.audio_file.url,
        }, status=201)

