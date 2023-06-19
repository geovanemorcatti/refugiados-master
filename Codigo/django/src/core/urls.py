"""
URL routes for the core app
"""

from django.urls import path, include
from . import views

app_name = 'core'
urlpatterns = [

    path('', include('django.contrib.auth.urls')),

    ########################
    ################# Main
    path('refugiados', views.refugiado_list, name='refugiado_list'),
    path('refugiados/cadastrar', views.refugiado_new, name='refugiado_new'),
    path('refugiados/importar', views.refugiado_bulk_import, name='refugiado_bulk_import'),
    path('refugiados/relatorio/<int:id>', views.refugiado_report, name='refugiado_report'),
    path('refugiados/editar/<int:id>', views.refugiado_edit, name='refugiado_edit'),
    path('refugiados/ficha/<int:id>', views.refugiado_ficha, name='refugiado_ficha'),
    path('refugiados/ficha/exportar/<int:id>', views.refugiado_ficha_export, name='refugiado_ficha_export'),
    path('refugiados/deletar/<int:id>', views.refugiado_delete, name='refugiado_delete'),

    #Report
    path('relatorios', views.report_geral, name='report_geral'),

    #Solicitacao
    path('solicitacoes/<int:ref_id>', views.solicitacao_new, name='solicitacao_new'),
    path('solicitacoes/detalhes/<int:id>', views.solicitacao_report, name='solicitacao_report'),
    path('solicitacoes/enviar/<int:id>', views.solicitacao_send, name='solicitacao_send'),
    path('solicitacoes/editar-texto/<int:id>', views.solicitacao_text_update, name='solicitacao_text_update'),
    path('solicitacoes/deletar/<int:id>', views.solicitacao_delete, name='solicitacao_delete'),

]