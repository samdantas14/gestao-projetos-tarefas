from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Projeto
from .forms import ProjetoForm

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