from django.urls import path
from .views import index, listar_cidades, previsao, CidadeCreate, PrevisaoList, exportar_previsoes_csv


app_name = "weather"
urlpatterns = [
    path("ola", index, name="index_view"),
    path("cidades", listar_cidades, name="cidades"),
    path("previsao/<int:pk>", previsao, name="previsao"),
    path("previsao/listar", PrevisaoList.as_view(), name="previsao_list"),
    path("previsao/exportar", exportar_previsoes_csv, name="previsao_exportar"),
    path("cidades/nova", CidadeCreate.as_view(), name="nova_cidade"),
]

