from django.urls import path
from . import views


urlpatterns = [
    path(
        "projetos/",
        views.lista_projetos,
        name="lista_projetos",
    ),
    path(
        "projetos/novo/",
        views.novo_projeto,
        name="novo_projeto",
    ),
]