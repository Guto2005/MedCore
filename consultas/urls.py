from django.urls import path

from . import views

urlpatterns = [

    path(
        '',
        views.listar_consultas,
        name='listar_consultas'
    ),

    path(
        'nova/',
        views.nova_consulta,
        name='nova_consulta'
    ),

    path(
        'editar/<int:id>/',
        views.editar_consulta,
        name='editar_consulta'
    ),

]