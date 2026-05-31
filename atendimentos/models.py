from django.db import models
from pacientes.models import Paciente
from medicos.models import Medico


class Atendimento(models.Model):
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE
    )

    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE
    )

    data_atendimento = models.DateTimeField(
        auto_now_add=True
    )

    queixa_principal = models.TextField()

    diagnostico = models.TextField()

    tratamento = models.TextField()

    observacoes = models.TextField(
        blank=True
    )

    retorno_recomendado = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.paciente.nome} - {self.data_atendimento}"