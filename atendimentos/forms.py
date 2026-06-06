from django import forms

from .models import Atendimento


class AtendimentoForm(forms.ModelForm):

    class Meta:

        model = Atendimento

        fields = [
            'paciente',
            'medico',
            'queixa_principal',
            'diagnostico',
            'tratamento',
            'observacoes',
            'retorno_recomendado',
            'status'
        ]

        widgets = {

            'queixa_principal': forms.Textarea(
                attrs={
                    'rows': 4
                }
            ),

            'diagnostico': forms.Textarea(
                attrs={
                    'rows': 4
                }
            ),

            'tratamento': forms.Textarea(
                attrs={
                    'rows': 4
                }
            ),

            'observacoes': forms.Textarea(
                attrs={
                    'rows': 4
                }
            ),

            'retorno_recomendado': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )

        }