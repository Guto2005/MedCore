from django.db import models


class Paciente(models.Model):
    SEXOS = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    nome = models.CharField(max_length=100)

    cpf = models.CharField(
        max_length=14,
        unique=True
    )

    data_nascimento = models.DateField()

    sexo = models.CharField(
        max_length=1,
        choices=SEXOS
    )

    telefone = models.CharField(max_length=20)

    telefone_emergencia = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    convenio = models.CharField(
        max_length=100,
        blank=True
    )

    alergias = models.TextField(
        blank=True
    )

    doencas_geneticas = models.TextField(
        blank=True
    )

    observacoes = models.TextField(
        blank=True
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nome