from django.shortcuts import render

def index(request):
    return render(request, 'anuncios/index.html')

def produtos(request):
    return render(request, 'anuncios/produtos.html')

def servicos(request):
    return render(request, 'anuncios/servicos.html')

def listaProdutos(request):
    return render(request, 'anuncios/lista_produtos.html')

def listaServicos(request):
    return render(request, 'anuncios/lista_servicos.html')

def detalhesProduto(request):
    return render(request, 'anuncios/detalhes_produto.html')

def detalhesProdutoOriginal(request):
    return render(request, 'anuncios/detalhes_produto_original.html')

def detalhesProdutoCarrossel(request):
    return render(request, 'anuncios/detalhes_produto_carrossel.html')

def detalhesServico(request):
    return render(request, 'anuncios/detalhes_servico.html')

def termosPrivacidade(request):
    return render(request, 'anuncios/termos_privacidade.html')
