from django.urls import path
from .views import login_view
from . import views

urlpatterns = [

    path(
        '',
        login_view,
        name='login'
    ),
    
       path(
        'perfil/',
        views.perfil,
        name='perfil'
    ),

    path(
        'alterar-senha/',
        views.alterar_senha,
        name='alterar_senha'
    ),

]