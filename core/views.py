from django.shortcuts import render, redirect
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