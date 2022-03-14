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


@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            Evento.objects.filter(id=id_evento).update(titulo=titulo,
                                                       data_evento=data_evento,
                                                       descricao=descricao)
        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario)
    return redirect('/')


@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user                 # validação para o usuario só poder excluir os seus eventos pertencentes
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()

    return redirect('/')

