from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('produtos/', views.produtos, name = 'produtos'),
    path('servicos/', views.servicos, name = 'servicos'),
    path('lista_produtos/', views.listaProdutos, name = 'lista_produtos'),
    path('lista_servicos/', views.listaServicos, name = 'lista_servicos'),
    path('detalhes_produto/', views.detalhesProduto, name = 'detalhes_produto'),
    path('detalhes_produto_original/', views.detalhesProdutoOriginal, name = 'detalhes_produto_original'),
    path('detalhes_produto_carrossel/', views.detalhesProdutoCarrossel, name = 'detalhes_produto_carrossel'),  
    path('detalhes_servico/', views.detalhesServico, name = 'detalhes_servico'),  
    path('termos_privacidade/', views.termosPrivacidade, name = 'termos_privacidade'),  
]
