from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.listar_atendimentos,
        name='listar_atendimentos'
    ),

    path(
        'novo/',
        views.novo_atendimento,
        name='novo_atendimento'
    ),
]