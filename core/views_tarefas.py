from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm


def lista_tarefas(request):
    tarefas = Tarefa.objects.select_related("projeto").all().order_by("concluido", "prioridade", "titulo")
    return render(request, "tarefas/lista.html", {"tarefas": tarefas})


def nova_tarefa(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_tarefas")
    else:
        form = TarefaForm()
    return render(request, "tarefas/formulario.html", {"form": form})


def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == "POST":
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect("lista_tarefas")
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, "tarefas/formulario.html", {"form": form, "tarefa": tarefa})


def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == "POST":
        tarefa.delete()
        return redirect("lista_tarefas")
    return render(request, "tarefas/confirmar_exclusao.html", {"tarefa": tarefa})
