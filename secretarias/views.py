from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Secretaria
from .forms import SecretariaForm


def listar_secretarias(request):

    secretarias = Secretaria.objects.all()

    return render(
        request,
        'secretarias/listar.html',
        {
            'secretarias': secretarias
        }
    )


def nova_secretaria(request):

    if request.method == 'POST':

        form = SecretariaForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'listar_secretarias'
            )

    else:

        form = SecretariaForm()

    return render(
        request,
        'secretarias/nova.html',
        {
            'form': form
        }
    )


def editar_secretaria(request, id):

    secretaria = get_object_or_404(
        Secretaria,
        id=id
    )

    if request.method == 'POST':

        form = SecretariaForm(
            request.POST,
            instance=secretaria
        )

        if form.is_valid():

            form.save()

            return redirect(
                'listar_secretarias'
            )

    else:

        form = SecretariaForm(
            instance=secretaria
        )

    return render(
        request,
        'secretarias/editar.html',
        {
            'form': form,
            'secretaria': secretaria
        }
    )