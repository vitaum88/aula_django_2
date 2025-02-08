from django.shortcuts import render


def home(request):
    return render(request, "aula_django/home.html")
