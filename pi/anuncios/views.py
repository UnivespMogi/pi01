from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Categoria, Produto, Servico, Contato

def index(request):
    return render(request, 'anuncios/index.html')

def produtos(request):
    categorias = Categoria.objects.filter(tp_categoria = 'P')
    return render(request, 'anuncios/produtos.html', {'categorias': categorias})

def servicos(request):
    categorias = Categoria.objects.filter(tp_categoria = 'S')
    return render(request, 'anuncios/servicos.html', {'categorias': categorias})

def listaProdutos(request,id):
    produtos = Produto.objects.filter(categoria=id)
    categoria = Categoria.objects.get(id=id)
    return render(request, 'anuncios/lista_produtos.html', {'produtos': produtos,'categoria':categoria})

def listaServicos(request,id):
    servicos = Servico.objects.filter(categoria=id)
    categoria = Categoria.objects.get(id=id)
    return render(request, 'anuncios/lista_servicos.html', {'servicos': servicos,'categoria':categoria})

def detalhesProduto(request,id):
    produto = Produto.objects.get(id=id)
    contato = Contato.objects.get()
    return render(request, 'anuncios/detalhes_produto.html', {'produto': produto,'contato' : contato})

def detalhesProdutoOriginal(request):
    return render(request, 'anuncios/detalhes_produto_original.html')

def detalhesProdutoCarrossel(request):
    return render(request, 'anuncios/detalhes_produto_carrossel.html')

def detalhesServico(request,id):
    servico = Servico.objects.get(id=id)
    contato = Contato.objects.get()
    return render(request, 'anuncios/detalhes_servico.html',{'servico':servico,'contato' : contato})


def politicaPrivacidade(request):
    return render(request, 'anuncios/politica_privacidade.html')

def faleConosco(request):
    return render(request, 'anuncios/fale_conosco.html')

def perguntasRespostas(request):
    return render(request, 'anuncios/perguntas_respostas.html')

def login(request):
    return render(request, 'anuncios/login.html')

def comoAnunciar(request):
    return render(request, 'anuncios/como_anunciar.html')

def politicaCookies(request):
    return render(request, 'anuncios/politica_cookies.html')

def termosUso(request):
    return render(request, 'anuncios/termos_uso.html')
