from django.db import models

from pacientes.models import Paciente
from medicos.models import Medico

class Consulta(models.Model):

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE
    )

    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE
    )

    data_hora = models.DateTimeField()

    observacoes = models.TextField(
        blank=True
    )

    STATUS_CHOICES = [

        ('AGENDADA', 'Agendada'),

        ('CONFIRMADA', 'Confirmada'),

        ('REALIZADA', 'Realizada'),

        ('FALTOU', 'Faltou'),

        ('CANCELADA', 'Cancelada'),

    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='AGENDADA'
    )

    def __str__(self):

        return f'{self.paciente.nome}'