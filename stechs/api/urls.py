from django.urls import path
from stechs.api.views import CableModemView

urlpatterns = [
    path("cable_modem/", CableModemView.as_view())
]
