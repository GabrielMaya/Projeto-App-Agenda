from django.shortcuts import render, redirect
from core.models import Evento
# Create your views here.


# def index(request):
#    return redirect('/agenda/')   # segunda opção redirecionamento de diretorio em branco na url


def lista_eventos(request):
    # usuario = request.user
    evento = Evento.objects.all()  # mostra todos os eventos cadastrados
    # evento = Evento.objects.filter(usuario=usuario)  # só vai retonar os eventos de cada usuário
    data = {'eventos' :evento}
    return render(request, 'agenda.html', data)
