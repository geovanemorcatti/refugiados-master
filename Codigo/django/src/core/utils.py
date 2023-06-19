from .models import Refugiado, Solicitacao, AcaoSolicitacao

def new_refugiado(payload):
  ref = Refugiado(
    nome = payload['name'],
    sexo = payload['gender'],
    idade = payload['age'],
    nacionalidade = payload['nationality'],
    formacao = payload['studyStatus'],
    profissao = payload['profession'],
    lingua = payload['lang'],
    pais = payload['country'],
    cidade = payload['city'],
    primeiro_destino = payload['firstDestination'],
    motivo_ida_brasil = payload['whyBrazil'],
    como_conheceu_projeto = payload['howMetProject'],
    servicos_que_procura = payload['servicesSought'],
    celular = payload['celular'],
    email = payload['email']
  )

  ref.save()


def edit_refugiado(payload, ref):
  ref.nome = payload['name']
  ref.sexo = payload['gender']
  ref.idade = payload['age']
  ref.nacionalidade = payload['nationality']
  ref.formacao = payload['studyStatus']
  ref.profissao = payload['profession']
  ref.lingua = payload['lang']
  ref.pais = payload['country']
  ref.cidade = payload['city']
  ref.primeiro_destino = payload['firstDestination']
  ref.motivo_ida_brasil = payload['whyBrazil']
  ref.como_conheceu_projeto = payload['howMetProject']
  ref.servicos_que_procura = payload['servicesSought'] 
  ref.celular = payload['celular']
  ref.email = payload['email']

  ref.save()
  return ref


def save_ficha_refugiado(payload, ref):
  ref.ficha_social = payload
  ref.save()
  return ref


def new_solicitacao(payload, ref_id, usr_id):
  sol = Solicitacao(
    refugiado_id = ref_id,
    usuario_id = usr_id,
    area_id = int(payload['area']),
    titulo = payload['titulo'],
    texto = payload['texto'],
    status = 'Criada'
  )

  sol.save()
  return sol


def change_solicitacao_status(payload, sol, usr_id):
  old_status = sol.status
  if old_status != payload['status']:
    sol.status = payload['status']
    act = AcaoSolicitacao(
      solicitacao_id = sol.id,
      usuario_id = usr_id,
      titulo = 'Alteração de status',
      texto = f'Alterado de {old_status} para {payload["status"]}'
    )
    act.save()
    sol.save()

  return sol

def update_solicitacao_text(payload, sol, usr_id):
  old_text = sol.texto
  if old_text != payload['text']:
    sol.texto = payload['text']
    act = AcaoSolicitacao(
      solicitacao_id = sol.id,
      usuario_id = usr_id,
      titulo = 'Alteração de texto',
      texto = 'Alteração no texto da solicitação'
    )
    act.save()
    sol.save()

  return sol
