from django.contrib.auth.models import User
from django.core import paginator
from django.shortcuts import render, redirect,get_object_or_404
from .models import Categoria, Produto, Servico, Contato
from random import shuffle
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect

from django.db.models import Q
from users.models import User
from .forms import ContactForm
from .forms import produto_Form
from django.contrib import messages

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'anuncios/index.html')

def produtos(request):
    categorias = Categoria.objects.filter(tp_categoria = 'P')
    return render(request, 'anuncios/produtos.html', {'categorias': categorias})

def servicos(request):
    categorias = Categoria.objects.filter(tp_categoria = 'S')
    return render(request, 'anuncios/servicos.html', {'categorias': categorias})

def listaProdutos(request,id):
    produtos = list(Produto.objects.filter(categoria=id,st_produto='A').order_by('dt_cadastro'))
    #shuffle(produtos)
    categoria = Categoria.objects.get(id=id)

    paginator = Paginator(produtos, 3)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'anuncios/lista_produtos.html', {'produtos': produtos,'categoria':categoria})

def listaServicos(request,id):
    servicos = list(Servico.objects.filter(categoria=id,st_servico='A'))
    #shuffle(servicos)
    categoria = Categoria.objects.get(id=id)

    paginator = Paginator(servicos, 3)
    page = request.GET.get('page')
    servicos = paginator.get_page(page)

    return render(request, 'anuncios/lista_servicos.html', {'servicos': servicos,'categoria':categoria})

def detalhesProduto(request  ,id ):
    produto = Produto.objects.get(id=id)
    contatos = Contato.objects.filter(usuario = produto.usuario)
    return render(request, 'anuncios/detalhes_produto.html', {'produto': produto,'contatos' : contatos})

def detalhesProdutoOriginal(request):
    return render(request, 'anuncios/detalhes_produto_original.html')

def detalhesProdutoCarrossel(request):
    return render(request, 'anuncios/detalhes_produto_carrossel.html')

def detalhesServico(request,id):
    servico = Servico.objects.get(id=id)
    contatos = Contato.objects.filter(usuario = servico.usuario)
    return render(request, 'anuncios/detalhes_servico.html',{'servico':servico,'contatos' : contatos})


def politicaPrivacidade(request):
    return render(request, 'anuncios/politica_privacidade.html')

def faleConosco(request):
    if request.method == 'GET':
        
        form = ContactForm()
    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            nome= form.cleaned_data['nome']
            assunto = form.cleaned_data['assunto']
            seu_email = form.cleaned_data['seu_email']
            mensagem = form.cleaned_data['mensagem']

            try:
                # send_mail ( subject , message )
                assunto = 'Teste (Fale conosco): '+ assunto
                mensagem = 'Nome:' + nome +'\nEmail:' + seu_email + '\nMensagem: ' + mensagem
                send_mail(assunto , mensagem, 'mogiunivesp5@hotmail.com', ['2005436@aluno.univesp.br','2011457@aluno.univesp.br' ])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ('Sucesso_envio_email')
    return render(request, 'anuncios/fale_conosco.html', {'form': form})

def Sucesso_envio_email(request):
    #return HttpResponse('Sucesso! Obrigado pela sua mensagem!')
    return render(request, 'anuncios/envio_email_sucesso.html')

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

def pesquisa(request):
    search = request.GET.get('search')

    if search:
        p1 = list(Produto.objects.filter(Q(nm_produto__contains=search) ))
        p2 = list(Servico.objects.filter(Q(dc_servico__contains=search) ))
        lista = p1 + p2
        #shuffle(lista)

    else:
        p1 = list(Produto.objects.all())
        p2 = list(Servico.objects.all())
        lista = p1 + p2

    paginator = Paginator(lista, 3)
    page = request.GET.get('page')
    anuncios = paginator.get_page(page)
    return render(request, 'anuncios/pesquisa.html', {'anuncios': anuncios})


def Cadastro_produto(request):
    produtos = Produto.objects.filter(usuario=request.user)
    return render(request, 'anuncios/Cadastro_produto.html', {'produtos': produtos})


@login_required
def Cadastro_servico(request):
    servicos = Servico.objects.filter(usuario=request.user)
    return render(request, 'anuncios/Cadastro_produto.html', {'servicos': servicos})

#@login_required
#def edit_produto(request, id):
    #task = get_object_or_404(Task, pk=id)
    #form = Produto_Form(instance=task)

    #if(request.method == 'POST'):
        #form = Produto_Form(request.POST, instance=task)

        #if(form.is_valid()):
            #task.save()
            #return redirect('/')
        #else:
            #return render(request, 'task/edittask.html', {'form': form, 'task': task})
    #else:
        #return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

@login_required
def produto_delete(request, id):
    produto = get_object_or_404(Produto, pk=id)
    #produto.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('Cadastro_produto')


@login_required
def produto_add(request):
    if request.method == 'POST':
        form = produto_Form(request.POST)
        
        if form.is_valid():
            Produto = form.save(commit=False)
            #Produto.done = 'doing'
            Produto.usuario = request.user
            Produto.save()
            return redirect('/')
    else:
        form = produto_Form()
        return render(request, 'anuncios/produto_add.html', {'form': form})

