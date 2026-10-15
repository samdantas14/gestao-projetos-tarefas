from django import forms
from .models import Projeto,Tarefa


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ["nome", "descricao", "data_inicio"]
        widgets = {
            "data_inicio": forms.DateInput(
                attrs={"type": "date"}
            ),
        }

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ["titulo", "prioridade", "concluido", "projeto"]
        widgets = {
            "data_inicio": forms.DateInput(
                attrs={"type": "date"}
            ),
        }