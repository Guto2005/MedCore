import pydicom
import numpy as np

from PIL import Image

from django.contrib import messages

from django.http import HttpResponse


from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import ExameForm
from .models import Exame
from django.core.paginator import Paginator

from .models import Laudo
from .forms_laudo import LaudoForm

from django.http import JsonResponse


def inbox_exames(request):

    lista_exames = Exame.objects.filter(
    status='PENDENTE'
    ).order_by(
        '-data_envio'
    )

    paginator = Paginator(
        lista_exames,
        15
    )

    page_number = request.GET.get(
        'page'
    )

    exames = paginator.get_page(
        page_number
    )

    return render(
        request,
        'exames/inbox.html',
        {
            'exames': exames
        }
    )


def exames_em_laudo(request):

    exames = Exame.objects.filter(
        status='EM_LAUDO'
    )

    return render(
        request,
        'exames/em_laudo.html',
        {
            'exames': exames
        }
    )


def exames_finalizados(request):

    exames = Exame.objects.filter(
        status='FINALIZADO'
    )

    return render(
        request,
        'exames/finalizados.html',
        {
            'exames': exames
        }
    )


def workspace_laudo(request, id):

    exame = get_object_or_404(
        Exame,
        id=id
    )

    laudo = Laudo.objects.filter(
        exame=exame
    ).first()

    # Salvaguarda temporária da 1.5 (registrada no MEDCORE_LAB.md):
    # exame FINALIZADO abre em modo consulta (sem edição), até a 1.6
    # implementar o fluxo real de auditoria/versionamento/reedição controlada.
    pode_editar = exame.status != 'FINALIZADO'

    if request.method == 'POST' and pode_editar:

        form = LaudoForm(
            request.POST,
            instance=laudo
        )

        if form.is_valid():

            novo_laudo = form.save(
                commit=False
            )

            novo_laudo.exame = exame

            novo_laudo.save()

            acao = request.POST.get(
                'acao'
            )

            if acao == 'finalizar':

                exame.status = 'FINALIZADO'

                exame.save()

                return redirect(
                    'exames_finalizados'
                )

            exame.status = 'EM_LAUDO'

            exame.save()

            return redirect(
                'workspace_laudo',
                id=exame.id
            )

    else:

        form = LaudoForm(
            instance=laudo
        )

    ds = pydicom.dcmread(
        exame.arquivo.path
    )

    return render(
        request,
        'exames/workspace_laudo.html',
        {
            'exame': exame,
            'form': form,
            'laudo': laudo,
            'pode_editar': pode_editar,
            'modalidade': ds.get(
                'Modality',
                'N/A'
            ),
            'rows': getattr(
                ds,
                'Rows',
                None
            ),
            'columns': getattr(
                ds,
                'Columns',
                None
            )
        }
    )
    
def importar_exame(request):

    if request.method == 'POST':

        form = ExameForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect(
                'inbox_exames'
            )

    else:

        form = ExameForm()

    return render(
        request,
        'exames/importar.html',
        {
            'form': form
        }
    )
    
def info_dicom(request, id):

    exame = get_object_or_404(
        Exame,
        id=id
    )

    ds = pydicom.dcmread(
        exame.arquivo.path
    )

    return JsonResponse({

        'paciente': str(
            ds.get(
                'PatientName',
                'Desconhecido'
            )
        ),

        'modalidade': str(
            ds.get(
                'Modality',
                'N/A'
            )
        ),

        'estudo': str(
            ds.get(
                'StudyDescription',
                'N/A'
            )
        ),

        'rows': getattr(
            ds,
            'Rows',
            None
        ),

        'columns': getattr(
            ds,
            'Columns',
            None
        ),

        'pixel_data': hasattr(
            ds,
            'PixelData'
        )

    })
    
def assumir_laudo(request, id):

    exame = get_object_or_404(
        Exame,
        id=id
    )

    if exame.status == 'PENDENTE':

        exame.status = 'EM_LAUDO'

        exame.save()

    return redirect(
        'workspace_laudo',
        id=exame.id
    )
    
def visualizar_dicom(request, id):

    exame = get_object_or_404(
        Exame,
        id=id
    )

    return render(
        request,
        'exames/visualizador.html',
        {
            'exame': exame
        }
    )

def preview_exame(request, id):

    exame = get_object_or_404(
        Exame,
        id=id
    )

    ds = pydicom.dcmread(
        exame.arquivo.path
    )

    pixels = ds.pixel_array

    pixels = pixels.astype(
        float
    )

    pixels = (
        np.maximum(
            pixels,
            0
        ) / pixels.max()
    ) * 255.0

    image = Image.fromarray(
        pixels.astype(
            np.uint8
        )
    )

    response = HttpResponse(
        content_type='image/png'
    )

    image.save(
        response,
        'PNG'
    )

    return response