from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from pacientes.models import Paciente
from medicos.models import Medico
from atendimentos.models import Atendimento


@login_required(login_url='login')
def home(request):

    context = {

        'total_pacientes': Paciente.objects.count(),

        'total_medicos': Medico.objects.count(),

        'total_atendimentos': Atendimento.objects.count(),

        'atendimentos_abertos': Atendimento.objects.filter(
            status='ABERTO'
        ).count(),

        'atendimentos_finalizados': Atendimento.objects.filter(
            status='FINALIZADO'
        ).count(),

        'atendimentos_cancelados': Atendimento.objects.filter(
            status='CANCELADO'
        ).count(),

        'ultimos_atendimentos': Atendimento.objects.select_related(
            'paciente',
            'medico',
            'medico__usuario'
        ).order_by(
            '-data_atendimento'
        )[:5]
    }

    return render(
        request,
        'dashboard/home.html',
        context
    )