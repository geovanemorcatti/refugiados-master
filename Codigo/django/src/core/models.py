from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Refugiado(models.Model):
  nome = models.CharField(max_length=120)
  sexo = models.CharField(max_length=20, 
    choices=[
      ('masc', 'Masculino'),
      ('fem', 'Feminino'),
      ('nb', 'Não-binário'),
      ('outro', 'Outro')
    ])
  idade = models.IntegerField()
  nacionalidade = models.CharField(max_length=120)
  formacao = models.CharField(max_length=120, default='', null=True, blank=True)
  profissao = models.CharField(max_length=120, default='', null=True, blank=True)
  lingua = models.CharField(max_length=120, default='', null=True, blank=True)
  pais = models.CharField(max_length=120, default='', null=True, blank=True)
  cidade = models.CharField(max_length=120, default='', null=True, blank=True)
  primeiro_destino = models.CharField(max_length=120, default='', null=True, blank=True)
  motivo_ida_brasil = models.TextField()
  como_conheceu_projeto = models.TextField()
  servicos_que_procura = models.TextField()
  celular = models.CharField(max_length=120, default='', null=True, blank=True)
  email = models.CharField(max_length=120, default='', null=True, blank=True)

  ficha_social = models.JSONField(null=True, blank=True)

  def to_template(self):
    return {
      'id': self.id,
      'name': self.nome,
      'gender': self.sexo,
      'age': self.idade,
      'nationality': self.nacionalidade,
      'studyStatus': self.formacao,
      'profession': self.profissao,
      'lang': self.lingua,
      'country': self.pais,
      'city': self.cidade,
      'firstDestination': self.primeiro_destino,
      'whyBrazil': self.motivo_ida_brasil,
      'howMetProject': self.como_conheceu_projeto,
      'servicesSought': self.servicos_que_procura,
      'phoneNumber': self.celular,
      'email': self.email
    }
  

class AreaAtendimento(models.Model):
  email = models.EmailField()
  nome = models.CharField(max_length=120)
  nome_instituicao = models.CharField(max_length=120, default='', blank=True, null=True)

  def to_template(self):
    return {
      'id': self.id,
      'email': self.email,
      'name': self.nome,
      'instName': self.nome_instituicao
    }
  
  def __str__(self):
    return f'{self.nome} - {self.email}'


class Solicitacao(models.Model):
  refugiado = models.ForeignKey(Refugiado, on_delete=models.CASCADE)
  usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  area = models.ForeignKey(AreaAtendimento, on_delete=models.CASCADE)
  data = models.DateTimeField(auto_now_add=True)
  titulo = models.CharField(max_length=120, default='', null=True, blank=True)
  texto = models.TextField()
  status = models.CharField(max_length=120, default='', null=True, blank=True)
  email_sent_to = models.CharField(max_length=120, default=None, null=True, blank=True)

  def to_template(self):
    area_name = self.area.nome if self.area is not None else ''
    area_email = self.area.email if self.area is not None else ''
    return {
      'id': self.id,
      'area': area_name,
      'areaEmail': area_email,
      'date': self.data.strftime('%d/%m/%Y %H:%M'),
      'title': self.titulo,
      'status': self.status,
      'text': self.texto,
      'user': self.usuario,
      'emailSent': self.email_sent_to
    }


class AcaoSolicitacao(models.Model):
  solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)
  usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  data = models.DateTimeField(auto_now_add=True)
  titulo = models.CharField(max_length=120, default='', null=True, blank=True)
  texto = models.TextField()

  def to_template(self):
    return {
      'id': self.id,
      'user': self.usuario,
      'date': self.data.strftime('%d/%m/%Y %H:%M'),
      'title': self.titulo,
      'text': self.texto,
      'refName': self.solicitacao.refugiado.nome,
      'areaName': self.solicitacao.area.nome
    }
