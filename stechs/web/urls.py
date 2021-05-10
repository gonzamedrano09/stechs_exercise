from django.urls import path
from stechs.web.views import index_tmpl

urlpatterns = [
    path("", index_tmpl, name="index_tmpl")
]
