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

    }

    return render(
        request,
        'dashboard/home.html',
        context
    )