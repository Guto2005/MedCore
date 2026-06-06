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

    path(
        '<int:atendimento_id>/',
        views.detalhes_atendimento,
        name='detalhes_atendimento'
    ),

]