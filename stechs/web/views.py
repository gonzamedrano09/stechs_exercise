from django.shortcuts import render


def index_tmpl(request):
    return render(request, "index.html")

