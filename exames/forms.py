from django import forms

from .models import Exame


class ExameForm(forms.ModelForm):

    class Meta:

        model = Exame

        fields = [
            'paciente',
            'tipo_exame',
            'arquivo'
        ]

        widgets = {

            'paciente': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'tipo_exame': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Raio-X de Tórax'
                }
            ),

            'arquivo': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'accept': '.dcm'
                }
            )

        }

    def clean_arquivo(self):

        arquivo = self.cleaned_data.get(
            'arquivo'
        )

        if not arquivo:

            raise forms.ValidationError(
                'Selecione um arquivo.'
            )

        extensao = arquivo.name.lower()

        if not extensao.endswith('.dcm'):

            raise forms.ValidationError(
                'Apenas arquivos DICOM (.dcm) são permitidos.'
            )

        return arquivo