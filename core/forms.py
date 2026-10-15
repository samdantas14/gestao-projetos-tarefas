
from django import forms
from .models import Projeto, Tarefa


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ["nome", "descricao", "data_inicio"]
        labels = {
            "nome": "Nome do projeto",
            "descricao": "Descrição",
            "data_inicio": "Data de início",
        }
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Ex.: Sistema acadêmico"}),
            "descricao": forms.Textarea(attrs={"placeholder": "Descreva o objetivo do projeto", "rows": 4}),
            "data_inicio": forms.DateInput(attrs={"type": "date"}),
        }


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ["titulo", "prioridade", "concluido", "projeto"]
        labels = {
            "titulo": "Título da tarefa",
            "prioridade": "Prioridade",
            "concluido": "Tarefa concluída",
            "projeto": "Projeto relacionado",
        }
        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "Ex.: Criar a página inicial"}),
        }

