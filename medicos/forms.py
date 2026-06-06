from django import forms

from .models import Medico
from usuarios.models import Usuario


class MedicoForm(forms.ModelForm):

    class Meta:

        model = Medico

        fields = [
            'usuario',
            'crm',
            'especialidade',
            'telefone'
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        usuarios_medicos = (
            Usuario.objects.filter(
                tipo_usuario='MEDICO'
            )
            .exclude(
                medico__isnull=False
            )
            .order_by('nome')
        )

        self.fields['usuario'].queryset = usuarios_medicos

        if not usuarios_medicos.exists():

            self.fields['usuario'].help_text = (
                'Nenhum usuário médico encontrado '
                'ou todos já possuem cadastro médico.'
            )