from django.shortcuts import render


def listar_medicos(request):

    return render(
        request,
        'medicos/listar.html'
    )


def cadastrar_medico(request):

    return render(
        request,
        'medicos/cadastrar.html'
    )