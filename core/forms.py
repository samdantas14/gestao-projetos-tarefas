from django import forms
from .models import Projeto


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ["nome", "descricao", "data_inicio"]
        widgets = {
            "data_inicio": forms.DateInput(
                attrs={"type": "date"}
            ),
        }