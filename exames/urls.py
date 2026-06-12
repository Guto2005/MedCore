from django.urls import path

from . import views

urlpatterns = [

    path(
        'detalhe/<int:id>/',
        views.detalhe_exame,
        name='detalhe_exame'
    ),
    
       path(
        'inbox/',
        views.inbox_exames,
        name='inbox_exames'
    ),

    path(
        'em-laudo/',
        views.exames_em_laudo,
        name='exames_em_laudo'
    ),

    path(
        'finalizados/',
        views.exames_finalizados,
        name='exames_finalizados'
    ),

    path(
        'detalhe/<int:id>/',
        views.detalhe_exame,
        name='detalhe_exame'
    ),
    
    path(
        'importar/',
        views.importar_exame,
        name='importar_exame'
    ),
    
    path(
        'info/<int:id>/',
        views.info_dicom,
        name='info_dicom'
    ),
    
    path(
        'visualizar/<int:id>/',
        views.visualizar_dicom,
        name='visualizar_dicom'
    ),
    
    path(
        'preview/<int:id>/',
        views.preview_exame,
        name='preview_exame'
    ),
    
    path(
        'assumir/<int:id>/',
        views.assumir_laudo,
        name='assumir_laudo'
    ),
]