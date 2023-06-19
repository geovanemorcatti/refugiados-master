from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Refugiado, Solicitacao, AreaAtendimento, AcaoSolicitacao

def send(area: AreaAtendimento, ref: Refugiado, details: str):
  html_message = render_to_string('email/default.html', {
    'ref': ref.to_template(),
    'dest': area.to_template(),
    'details': details
    })
  plain_message = strip_tags(html_message)
  send_mail(
    'Encaminhamento de demanda - Cátedra SVM PUC Minas',
    plain_message,
    'catedra.svm.puc.minas@gmail.com',
    [area.email],
    html_message=html_message
  )


def record_changes(area: AreaAtendimento, sol: Solicitacao, usr_id: int):
  sol.status = 'Encaminhada'
  sol.email_sent_to = area.email
  act = AcaoSolicitacao(
    solicitacao_id = sol.id,
    usuario_id = usr_id,
    titulo = 'Encaminhamento',
    texto = f'Solicitação encaminhada para {area.nome} no e-mail {area.email}'
  )
  act.save()
  sol.save()
  return sol


def process_request(sol: Solicitacao, usr_id: int):
  if sol.status == 'Encaminhada':
    return sol
  area = sol.area
  ref = sol.refugiado
  send(area.email, ref, sol.texto)
  new_sol = record_changes(area, sol, usr_id)
  return new_sol

