from django.db import models
from usuarios.models import Usuario


class Medico(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE
    )

    crm = models.CharField(
        max_length=20,
        unique=True
    )

    especialidade = models.CharField(
        max_length=100
    )

    telefone = models.CharField(
        max_length=20
    )

    def __str__(self):
        return f"{self.usuario.nome} - {self.especialidade}"