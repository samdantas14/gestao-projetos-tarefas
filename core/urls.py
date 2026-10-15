
from django.urls import path
from . import views
from . import views_tarefas

urlpatterns = [
    path("projetos/", views.lista_projetos, name="lista_projetos"),
    path("projetos/novo/", views.novo_projeto, name="novo_projeto"),
    path("projetos/<int:pk>/editar/", views.editar_projeto, name="editar_projeto"),
    path("projetos/<int:pk>/excluir/", views.excluir_projeto, name="excluir_projeto"),
    path("tarefas/", views_tarefas.lista_tarefas, name="lista_tarefas"),
    path("tarefas/nova/", views_tarefas.nova_tarefa, name="nova_tarefa"),
    path("tarefas/<int:pk>/editar/", views_tarefas.editar_tarefa, name="editar_tarefa"),
    path("tarefas/<int:pk>/excluir/", views_tarefas.excluir_tarefa, name="excluir_tarefa"),
]
