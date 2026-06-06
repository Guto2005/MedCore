from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.db.models import Q

from .models import Medico
from .forms import MedicoForm


def listar_medicos(request):

    busca = request.GET.get(
        'busca',
        ''
    )

    medicos = Medico.objects.select_related(
        'usuario'
    )

    if busca:

        medicos = medicos.filter(

            Q(usuario__nome__icontains=busca)

            |

            Q(crm__icontains=busca)

            |

            Q(especialidade__icontains=busca)

        )

    medicos = medicos.order_by(
        'usuario__nome'
    )

    return render(
        request,
        'medicos/listar.html',
        {
            'medicos': medicos,
            'busca': busca
        }
    )


def cadastrar_medico(request):

    if request.method == 'POST':

        form = MedicoForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            acao = request.POST.get(
                'acao'
            )

            if acao == 'novo':

                return redirect(
                    'cadastrar_medico'
                )

            return redirect(
                'listar_medicos'
            )

    else:

        form = MedicoForm()

    return render(
        request,
        'medicos/cadastrar.html',
        {
            'form': form
        }
    )


def detalhes_medico(
    request,
    medico_id
):

    medico = get_object_or_404(
        Medico,
        id=medico_id
    )

    return render(
        request,
        'medicos/detalhes.html',
        {
            'medico': medico
        }
    )