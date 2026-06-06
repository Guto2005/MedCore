from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.db.models import Q

from .models import Atendimento
from .forms import AtendimentoForm


def listar_atendimentos(request):

    busca = request.GET.get(
        'busca',
        ''
    )

    atendimentos = (
        Atendimento.objects
        .select_related(
            'paciente',
            'medico',
            'medico__usuario'
        )
    )

    if busca:

        atendimentos = atendimentos.filter(

            Q(
                paciente__nome__icontains=busca
            )

            |

            Q(
                medico__usuario__nome__icontains=busca
            )

        )

    atendimentos = atendimentos.order_by(
        '-data_atendimento'
    )

    return render(
        request,
        'atendimentos/listar.html',
        {
            'atendimentos': atendimentos,
            'busca': busca
        }
    )


def novo_atendimento(request):

    if request.method == 'POST':

        form = AtendimentoForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            acao = request.POST.get(
                'acao'
            )

            if acao == 'novo':

                return redirect(
                    'novo_atendimento'
                )

            return redirect(
                'listar_atendimentos'
            )

    else:

        form = AtendimentoForm()

    return render(
        request,
        'atendimentos/novo.html',
        {
            'form': form
        }
    )


def detalhes_atendimento(
    request,
    atendimento_id
):

    atendimento = get_object_or_404(
        Atendimento,
        id=atendimento_id
    )

    return render(
        request,
        'atendimentos/detalhes.html',
        {
            'atendimento': atendimento
        }
    )