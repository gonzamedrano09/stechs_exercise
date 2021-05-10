from django.urls import path, include

urlpatterns = [
    path("", include("stechs.web.urls")),
    path("api/", include("stechs.api.urls"))
]
