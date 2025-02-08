from django.urls import path
from .views import index, listar_cidades


app_name = "weather"
urlpatterns = [
    path("ola", index, name="index_view"),
    path("cidades", listar_cidades, name="cidades")
]

