from django.shortcuts import render


def home(request):
    return render(request, "pages/index.html")


def catalog(request):
    return render(request, "pages/catalog.html")


def offerts(request):
    return render(request, "pages/offerts.html")


def oforms(request):
    return render(request, "pages/oforms.html")


def socseti(request):
    return render(request, "pages/socseti.html")


def checkpvz(request):
    return render(request, "pages/checkpvz.html")


def checkdanzak(request):
    return render(request, "pages/checkdanzak.html")
