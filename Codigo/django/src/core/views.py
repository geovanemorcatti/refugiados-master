from datetime import datetime
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import AcaoSolicitacao, Refugiado, Solicitacao, AreaAtendimento
from . import utils
from . import mail
from .excel.handler import export_to_xls, import_from_xls

############################
## Refugiados
###########################

@login_required(login_url='/sistema/login')
def refugiado_list(request):
  template = loader.get_template('list.html')
    
  raw_list = Refugiado.objects.all().order_by('id')
  filtered_list = []
  for ref in raw_list:
    filtered_list.append(ref.to_template())

  context = {
      'refugiados': filtered_list
  }
  return HttpResponse(template.render(context, request))


@login_required(login_url='/sistema/login')
def refugiado_new(request):
  template = loader.get_template('new.html')
  created = False

  if request.method == 'POST':
    utils.new_refugiado(request.POST)
    created = True

  context = {
      'created': created,
  }
  return HttpResponse(template.render(context, request))


@login_required(login_url='/sistema/login')
def refugiado_report(request, id):
  template = loader.get_template('report.html')
  edited = False

  ref = get_object_or_404(Refugiado, pk=id)
  
  sol_list_raw = Solicitacao.objects.filter(refugiado=ref)
  sol_list = []
  for sol in sol_list_raw:
    sol_list.append(sol.to_template())

  context = {
      'ref': ref.to_template(),
      'sol_list': sol_list,
      'edited': edited
  }
  return HttpResponse(template.render(context, request))


@login_required(login_url='/sistema/login')
def refugiado_edit(request, id):
  template = loader.get_template('edit.html')
  edited = False

  ref = get_object_or_404(Refugiado, pk=id)

  if request.method == 'POST':
    ref = utils.edit_refugiado(request.POST, ref)
    edited = True

  context = {
      'ref': ref.to_template(),
      'edited': edited
  }
  return HttpResponse(template.render(context, request))


@login_required(login_url='/sistema/login')
def refugiado_delete(request, id):
  ref = get_object_or_404(Refugiado, pk=id)

  filtered_list = []
  if request.method == 'POST':
    template = loader.get_template('list.html')
    ref.delete()
    deleted = True
    raw_list = Refugiado.objects.all().order_by('id')
    for ref in raw_list:
      filtered_list.append(ref.to_template())
  else:
    template = loader.get_template('delete.html')
    deleted = False

  context = {
      'refugiados': filtered_list,
      'ref': ref.to_template(),
      'deleted': deleted
  }
  return HttpResponse(template.render(context, request))


############################
## Solicitações
###########################
@login_required(login_url='/sistema/login')
def solicitacao_new(request, ref_id):
  template = loader.get_template('solicitacao/new.html')
  created = False
  sol_id = None

  usr = request.user

  ref = get_object_or_404(Refugiado, pk=ref_id)
  area_list_raw = AreaAtendimento.objects.all().order_by('nome')
  area_list = []
  for area in area_list_raw:
    area_list.append(area.to_template())

  if request.method == 'POST':
    created = True
    sol_id = utils.new_solicitacao(request.POST, ref_id, usr.id)


  context = {
      'ref': ref.to_template(),
      'created': created,
      'area_list': area_list,
      'sol_id': sol_id
  }
  return HttpResponse(template.render(context, request))


@login_required(login_url='/sistema/login')
def solicitacao_report(request, id):
  template = loader.get_template('solicitacao/report.html')
  edited = False
  sol_id = None

  usr = request.user

  sol = get_object_or_404(Solicitacao, pk=id)
  ref = sol.refugiado
  
  if request.method == 'POST':
    edited = True
    sol = utils.change_solicitacao_status(request.POST, sol, usr.id)

  act_raw = AcaoSolicitacao.objects.filter(solicitacao=sol)
  act_list = []
  for act in act_raw:
    act_list.append(act.to_template())

  context = {
      'ref': ref.to_template(),
      'sol': sol.to_template(),
      'act_list': act_list,
      'edited': edited,
      'sol_id': sol_id,
      'sent': False
  }
  return HttpResponse(template.render(context, request))


@login_required(login_url='/sistema/login')
def solicitacao_text_update(request, id):
  sol = get_object_or_404(Solicitacao, pk=id)
  usr = request.user
  if request.method == 'POST':
    sol = utils.update_solicitacao_text(request.POST, sol, usr.id)
  
  return redirect(f'/sistema/solicitacoes/detalhes/{id}')


@login_required(login_url='/sistema/login')
def solicitacao_send(request, id):
  template = loader.get_template('solicitacao/report.html')
  sol = get_object_or_404(Solicitacao, pk=id)
  ref = sol.refugiado
  usr = request.user

  if request.method == 'POST':
    sol = mail.process_request(sol, usr.id)

  act_raw = AcaoSolicitacao.objects.filter(solicitacao=sol)
  act_list = []
  for act in act_raw:
    act_list.append(act.to_template())
  

  context = {
      'ref': ref.to_template(),
      'sol': sol.to_template(),
      'act_list': act_list,
      'edited': False,
      'sol_id': sol.id,
      'sent': True
  }
  return HttpResponse(template.render(context, request))


@login_required(login_url='/sistema/login')
def solicitacao_delete(request, id):
  sol = get_object_or_404(Solicitacao, pk=id)
  ref = sol.refugiado

  if request.method == 'POST':
    template = loader.get_template('report.html')
    sol.delete()
    redirect('refugiado_report', id=ref.id)
    return redirect(f'/sistema/refugiados/relatorio/{ref.id}')
  else:
    template = loader.get_template('solicitacao/delete.html')
    deleted = False

  context = {
    'sol': sol
  }
  return HttpResponse(template.render(context, request))


@login_required(login_url='/sistema/login')
def report_geral(request):
  template = loader.get_template('general-report.html')
  area_list_raw = AreaAtendimento.objects.all().order_by('nome')
  area_list = []
  for area in area_list_raw:
    area_list.append(area.to_template())

  filter = {
    'date_min': None,
    'date_max': None,
    'area': None
  }

  filter_args = {
    'titulo': 'Encaminhamento'
  }
  if request.method == 'POST':
    if len(request.POST.get('date_min', '')) > 0:
      d_min = datetime.strptime(request.POST.get('date_min'), '%Y-%m-%d')
      filter_args['data__gte'] = d_min
      filter['date_min'] = d_min.strftime('%Y-%m-%d')
    if len(request.POST.get('date_max', '')) > 0:
      d_max = datetime.strptime(request.POST.get('date_max'), '%Y-%m-%d')
      filter_args['data__lte'] = d_max
      filter['date_max'] = d_max.strftime('%Y-%m-%d')
    if request.POST.get('area', 'NULL') != 'NULL':
      filter_args['solicitacao__area_id'] = request.POST.get('area', 1)
      filter['area'] = request.POST.get('area', 1)

  acao_list = []
  query = AcaoSolicitacao.objects.filter(**filter_args).order_by('data')
  for acao in query:
    acao_list.append(acao.to_template())

  context = {
    'acao_list': acao_list,
    'area_list': area_list,
    'filter': filter
  }
  return HttpResponse(template.render(context, request))


@login_required(login_url='/sistema/login')
def refugiado_ficha(request, id):
  template = loader.get_template('ficha-details.html')
  edited = False

  ref = get_object_or_404(Refugiado, pk=id)

  if request.method == 'POST':
    ref = utils.save_ficha_refugiado(request.POST, ref)
    edited = True

  context = {
      'main': ref.to_template(),
      'ref': ref.ficha_social,
      'edited': edited
  }
  return HttpResponse(template.render(context, request))


@login_required(login_url='/sistema/login')
def refugiado_ficha_export(request, id):
  ref = get_object_or_404(Refugiado, pk=id)

  return export_to_xls(ref.ficha_social, ref)


@login_required(login_url='/sistema/login')
def refugiado_bulk_import(request):
  template = loader.get_template('bulk-import.html')
  
  edited = False
  import_count = 0

  if request.method == 'POST':
    print(request.FILES)
    edited = True
    import_count = import_from_xls(request.FILES['file'].file)

  context = {
      'edited': edited,
      'import_count': import_count
  }
  return HttpResponse(template.render(context, request))
