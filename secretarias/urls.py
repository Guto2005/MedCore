from django.urls import path

from . import views

urlpatterns = [

    path(
        'listar/',
        views.listar_secretarias,
        name='listar_secretarias'
    ),

    path(
        'nova/',
        views.nova_secretaria,
        name='nova_secretaria'
    ),
    
   path(
        'editar/<int:id>/',
        views.editar_secretaria,
        name='editar_secretaria'
    ),

]