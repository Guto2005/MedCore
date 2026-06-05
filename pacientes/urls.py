from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.listar_pacientes,
        name='listar_pacientes'
    ),

    path(
        'cadastrar/',
        views.cadastrar_paciente,
        name='cadastrar_paciente'
    ),
]