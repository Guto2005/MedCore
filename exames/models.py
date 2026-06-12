from django.db import models

from pacientes.models import Paciente


class Exame(models.Model):

    STATUS_CHOICES = [

        ('PENDENTE', 'Pendente'),
        ('EM_LAUDO', 'Em Laudo'),
        ('FINALIZADO', 'Finalizado')

    ]

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE
    )

    tipo_exame = models.CharField(
        max_length=100
    )

    arquivo = models.FileField(
        upload_to='exames/'
    )

    data_envio = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDENTE'
    )

    def __str__(self):

        return f"{self.paciente.nome} - {self.tipo_exame}"


class Laudo(models.Model):

    exame = models.OneToOneField(
        Exame,
        on_delete=models.CASCADE
    )

    diagnostico = models.TextField()

    observacoes = models.TextField(
        blank=True
    )

    data_laudo = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"Laudo #{self.exame.id}"