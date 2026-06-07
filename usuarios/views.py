from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AlterarSenhaForm
from django.contrib.auth import update_session_auth_hash


@login_required
def perfil(request):

    return render(
        request,
        'usuarios/perfil.html'
    )

def login_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        messages.error(
            request,
            'Usuário ou senha inválidos.'
        )

    return render(
        request,
        'usuarios/login.html'
    )
    
@login_required
def alterar_senha(request):

    if request.method == 'POST':

        form = AlterarSenhaForm(
            request.user,
            request.POST
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                'Senha alterada com sucesso.'
            )

            return redirect(
                'alterar_senha'
            )

    else:

        form = AlterarSenhaForm(
            request.user
        )
    return render(
        request,
        'usuarios/alterar_senha.html',
        {
            'form': form
        }
    )