from django.views import View
from django.http import HttpResponse


class CableModemView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")
