from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente

        fields = [
            'nome',
            'cpf',
            'data_nascimento',
            'sexo',
            'telefone',
            'telefone_emergencia',
            'email',
            'convenio',
            'alergias',
            'doencas_geneticas',
            'observacoes',
        ]

        widgets = {
            'data_nascimento': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )
        }