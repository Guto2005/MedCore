from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.db.models import Q

from .models import Paciente
from .forms import PacienteForm


def listar_pacientes(request):

    busca = request.GET.get('busca', '')

    pacientes = Paciente.objects.all()

    if busca:

        pacientes = pacientes.filter(
            Q(nome__icontains=busca) |
            Q(cpf__icontains=busca)
        )

    pacientes = pacientes.order_by('nome')

    return render(
        request,
        'pacientes/listar.html',
        {
            'pacientes': pacientes,
            'busca': busca
        }
    )


def cadastrar_paciente(request):

    if request.method == 'POST':

        form = PacienteForm(request.POST)

        if form.is_valid():

            form.save()

            acao = request.POST.get('acao')

            if acao == 'novo':

                return redirect(
                    'cadastrar_paciente'
                )

            return redirect(
                'listar_pacientes'
            )

    else:

        form = PacienteForm()

    return render(
        request,
        'pacientes/cadastrar.html',
        {
            'form': form
        }
    )


def detalhes_paciente(request, paciente_id):

    paciente = get_object_or_404(
        Paciente,
        id=paciente_id
    )

    return render(
        request,
        'pacientes/detalhes.html',
        {
            'paciente': paciente
        }
    )