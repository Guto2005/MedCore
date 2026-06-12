from django import forms

from .models import Laudo


class LaudoForm(forms.ModelForm):

    class Meta:

        model = Laudo

        fields = [
            'diagnostico',
            'observacoes'
        ]

        widgets = {

            'diagnostico': forms.Textarea(
                attrs={
                    'rows': 10
                }
            ),

            'observacoes': forms.Textarea(
                attrs={
                    'rows': 5
                }
            )
        }