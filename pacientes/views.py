from django.shortcuts import render


def listar_pacientes(request):

    return render(
        request,
        'pacientes/listar.html'
    )


def cadastrar_paciente(request):

    return render(
        request,
        'pacientes/cadastrar.html'
    )