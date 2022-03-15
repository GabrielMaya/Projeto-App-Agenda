from django.db import models
from django.contrib.auth.models import User   # Importando módulos do Django (nesse caso o user)
from datetime import datetime, timedelta

# Create your models here.
# sempre que modificar uma classe, precisa atualizar no banco. Terminal: makemigrations core

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)   # usando o user do Django para ditar usuário
                                                                    # models.CASCADE = Se o usuario for deletado apaga todos os eventos relacionados a ele

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y ás %H:%M Hrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False






