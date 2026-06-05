from django.shortcuts import render


def listar_atendimentos(request):

    return render(
        request,
        'atendimentos/listar.html'
    )


def novo_atendimento(request):

    return render(
        request,
        'atendimentos/novo.html'
    )