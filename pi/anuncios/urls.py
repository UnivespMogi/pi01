from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('produtos/', views.produtos, name = 'produtos'),
    path('servicos/', views.servicos, name = 'servicos'),
    path('lista_produtos/<int:id>', views.listaProdutos, name = 'lista_produtos'),
    path('lista_servicos/<int:id>', views.listaServicos, name = 'lista_servicos'),
    path('detalhes_produto/<int:id>', views.detalhesProduto, name = 'detalhes_produto'),
    path('detalhes_produto_original/', views.detalhesProdutoOriginal, name = 'detalhes_produto_original'),
    path('detalhes_produto_carrossel/', views.detalhesProdutoCarrossel, name = 'detalhes_produto_carrossel'),  
    path('detalhes_servico/<int:id>/', views.detalhesServico, name = 'detalhes_servico'),  
    path('politica_privacidade/', views.politicaPrivacidade, name = 'politica_privacidade'),  
    path('Sucesso_envio_email/', views.Sucesso_envio_email, name='Sucesso_envio_email'),
    path('Cadastro_produto/', views.Cadastro_produto, name='Cadastro_produto'),
    path('Cadastro_contato/', views.Cadastro_contato, name='Cadastro_contato'),

    path('fale_conosco/', views.faleConosco, name = 'fale_conosco'),  
    path('perguntas_respostas/', views.perguntasRespostas, name = 'perguntas_respostas'),  
    #path('login/', views.login, name = 'login'),  


    path('como_anunciar/', views.comoAnunciar, name = 'como_anunciar'),  
    path('politica_cookies/', views.politicaCookies, name = 'politica_cookies'),  
    path('termos_uso/', views.termosUso, name = 'termos_uso'),  

    path('pesquisa/', views.pesquisa, name = 'pesquisa'),
    
    path('produto_delete/<int:id>', views.produto_delete, name='produto_delete'),
    path('produto_add/', views.produto_add, name='produto_add'),
    path('produto_edit/<int:id>', views.produto_edit, name='produto_edit')

]


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
