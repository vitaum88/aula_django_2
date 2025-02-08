from django.shortcuts import render, get_object_or_404
from weather.models import Cidade
from weather.utils import get_weather


def index(request):
    cidades = Cidade.objects.all()
    return render(
        request, template_name="weather/index.html", context={"cidades": cidades})


def listar_cidades(request):
    cidades = Cidade.objects.all()
    return render(
        request, template_name="weather/lista_cidades.html", context={"cidades": cidades})


def previsao(request, cidade_id):
    cidade = get_object_or_404(Cidade, pk=cidade_id)
    previsoes = get_weather(cidade)
    return render(
        request, template_name="weather/previsao.html", context={"cidade": cidade, "previsoes": previsoes})
