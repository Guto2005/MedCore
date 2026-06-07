from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Consulta
from .forms import ConsultaForm


def listar_consultas(request):

    consultas = Consulta.objects.select_related(
        'paciente',
        'medico',
        'medico__usuario'
    ).order_by(
        '-data_hora'
    )

    return render(
        request,
        'consultas/listar.html',
        {
            'consultas': consultas
        }
    )


def nova_consulta(request):

    if request.method == 'POST':

        form = ConsultaForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'listar_consultas'
            )

    else:

        form = ConsultaForm()

    return render(
        request,
        'consultas/nova.html',
        {
            'form': form
        }
    )


def editar_consulta(request, id):

    consulta = get_object_or_404(
        Consulta,
        id=id
    )

    if request.method == 'POST':

        form = ConsultaForm(
            request.POST,
            instance=consulta
        )

        if form.is_valid():

            form.save()

            return redirect(
                'listar_consultas'
            )

    else:

        form = ConsultaForm(
            instance=consulta
        )

    return render(
        request,
        'consultas/nova.html',
        {
            'form': form
        }
    )