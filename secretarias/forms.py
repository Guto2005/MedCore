from django import forms
from .models import Secretaria


class SecretariaForm(forms.ModelForm):

    medicos = forms.ModelMultipleChoiceField(

        queryset=None,

        widget=forms.CheckboxSelectMultiple,

        label='Médicos Vinculados'
    )

    class Meta:

        model = Secretaria

        fields = [
            'usuario',
            'medicos'
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        from medicos.models import Medico

        self.fields['medicos'].queryset = Medico.objects.all()