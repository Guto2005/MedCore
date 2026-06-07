from django.db import models

from usuarios.models import Usuario
from medicos.models import Medico


class Secretaria(models.Model):

    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE
    )

    medicos = models.ManyToManyField(
        Medico,
        related_name='secretarias'
    )

    def __str__(self):

        return self.usuario.nome