from django.db import models


class Usuario(models.Model):
    TIPOS_USUARIO = [
        ('ADMIN', 'Administrador'),
        ('MEDICO', 'Médico'),
        ('USUARIO', 'Usuário'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPOS_USUARIO,
        default='USUARIO'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome