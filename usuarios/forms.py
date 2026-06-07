from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import re


class AlterarSenhaForm(PasswordChangeForm):

    old_password = PasswordChangeForm.base_fields['old_password']
    new_password1 = PasswordChangeForm.base_fields['new_password1']
    new_password2 = PasswordChangeForm.base_fields['new_password2']

    old_password.label = _('Senha Atual')
    new_password1.label = _('Nova Senha')
    new_password2.label = _('Confirmar Nova Senha')

    old_password.help_text = ''
    new_password2.help_text = ''

    new_password1.help_text = """
    <ul>
        <li>Mínimo de 8 caracteres.</li>
        <li>Pelo menos uma letra maiúscula.</li>
        <li>Pelo menos uma letra minúscula.</li>
        <li>Pelo menos um número.</li>
        <li>Pelo menos um caractere especial.</li>
        <li>Não pode ser igual à senha atual.</li>
    </ul>
    """

    def clean_new_password1(self):

        senha = self.cleaned_data.get('new_password1')

        if not senha:
            return senha

        # Não permite repetir a senha atual
        if self.user.check_password(senha):

            raise ValidationError(
                'A nova senha deve ser diferente da senha atual.'
            )

        # Mínimo de 8 caracteres
        if len(senha) < 8:

            raise ValidationError(
                'A senha deve possuir pelo menos 8 caracteres.'
            )

        # Letra maiúscula
        if not re.search(r'[A-Z]', senha):

            raise ValidationError(
                'A senha deve conter pelo menos uma letra maiúscula.'
            )

        # Letra minúscula
        if not re.search(r'[a-z]', senha):

            raise ValidationError(
                'A senha deve conter pelo menos uma letra minúscula.'
            )

        # Número
        if not re.search(r'\d', senha):

            raise ValidationError(
                'A senha deve conter pelo menos um número.'
            )

        # Caractere especial
        if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', senha):

            raise ValidationError(
                'A senha deve conter pelo menos um caractere especial.'
            )

        return senha