from django import forms

from .models import Consulta


class ConsultaForm(forms.ModelForm):

    class Meta:

        model = Consulta

        fields = [
            'paciente',
            'medico',
            'data_hora',
            'observacoes',
            'status'
        ]

        widgets = {

            'data_hora': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local'
                }
            ),

            'observacoes': forms.Textarea(
                attrs={
                    'rows': 4
                }
            )

        }