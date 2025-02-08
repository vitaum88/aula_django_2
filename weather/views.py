import csv
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from weather.models import Cidade, Previsao
from weather.utils import get_weather


def index(request):
    cidades = Cidade.objects.all()
    return render(
        request, template_name="weather/index.html", context={"cidades": cidades})


def listar_cidades(request):
    cidades = Cidade.objects.all()
    return render(
        request, template_name="weather/lista_cidades.html", context={"cidades": cidades})


def previsao(request, pk):
    cidade = get_object_or_404(Cidade, pk=pk)
    res = get_weather(cidade.lat, cidade.long)
    prev, _ = Previsao.objects.get_or_create(
        cidade=cidade,
        data=res[0],
        temp_max=res[1],
        temp_min=res[2]
    )
    return render(
        # request, template_name="weather/previsao.html", context={"cidade": cidade, "previsao": res}
        request, template_name="weather/previsao.html", context={"cidade": cidade, "previsao": prev}
    )


class CidadeCreate(CreateView):
    model = Cidade
    fields = ["nome", "estado", "pais", "lat", "long"]
    template_name = "weather/cidade_form.html"
    success_url = reverse_lazy("weather:cidades")


class PrevisaoList(ListView):
    model = Previsao
    template_name = "weather/lista_previsoes.html"
    context_object_name = "previsoes"
    ordering = ["cidade", "data"]


def exportar_previsoes_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="previsoes.csv"'

    writer = csv.writer(response)
    writer.writerow(['Cidade', 'Data', 'Temp. Máx', 'Temp. Mín'])
    previsoes = Previsao.objects.all().order_by('cidade', 'data')

    for previsao in previsoes:
        writer.writerow([previsao.cidade, previsao.data, previsao.temp_max, previsao.temp_min])

    return response
