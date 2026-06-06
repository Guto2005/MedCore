from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.listar_medicos,
        name='listar_medicos'
    ),

    path(
        'cadastrar/',
        views.cadastrar_medico,
        name='cadastrar_medico'
    ),

    path(
        '<int:medico_id>/',
        views.detalhes_medico,
        name='detalhes_medico'
    ),

]