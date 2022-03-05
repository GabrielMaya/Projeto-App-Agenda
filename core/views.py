from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required  # para só acessar uma página se estiver logado
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# def index(request):
#    return redirect('/agenda/')   # segunda opção redirecionamento de diretorio em branco na url

def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")

    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    user = request.user
    # evento = Evento.objects.all()  # mostra todos os eventos cadastrados
    evento = Evento.objects.filter(usuario=usuario)  # só vai retonar os eventos de cada usuário
    data = {'eventos': evento}
    return render(request, 'agenda.html', data)
