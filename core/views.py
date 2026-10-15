from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Projeto,Tarefa
from .forms import ProjetoForm,TarefaForm

def lista_projetos(request):
    projetos = Projeto.objects.all().order_by("nome")

    return render(
        request,
        "projetos/lista.html",
        {"projetos": projetos},
    )

def novo_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista_projetos")
    else:
        form = ProjetoForm()

    return render(
        request,
        "projetos/formulario.html",
        {"form": form},
    )

def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == "POST":
        form = ProjetoForm(request.POST, instance=projeto)

        if form.is_valid():
            form.save()
            return redirect("lista_projetos")
    else:
        form = ProjetoForm(instance=projeto)

    return render(
        request,
        "projetos/formulario.html",
        {
            "form": form,
            "projeto": projeto,
        },
    )

def excluir_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == "POST":
        projeto.delete()
        return redirect("lista_projetos")

    return render(
        request,
        "projetos/confirmar_exclusao.html",
        {"projeto": projeto},
    )

def lista_tarefas(request):

    tarefas = Tarefa.objects.all()

    return render(
        request,
        'core/tarefa_lista.html',
        {'tarefas': tarefas}
    )

def nova_tarefa(request):

    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('lista_tarefas')

    else:
        form = TarefaForm()

    return render(
        request,
        'core/tarefa_form.html',
        {'form': form}
    )

def editar_tarefa(request, pk):

    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)

        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('lista_tarefas')

    else:
        form = TarefaForm(instance=tarefa)

    return render(
        request,
        'core/tarefa_form.html',
        {'form': form}
    )

def excluir_tarefa(request, pk):

    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('lista_tarefas')

    return redirect('lista_tarefas')

