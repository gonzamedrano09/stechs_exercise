from django.urls import path
from stechs.api.views import CableModemView

urlpatterns = [
    path("cable_modems/", CableModemView.as_view())
]
