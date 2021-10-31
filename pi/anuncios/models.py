from django.db import models
from django.contrib import admin
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.fields import CharField, DateTimeField

# Categoria


class Categoria(models.Model):
    STATUS_CHOICES = (
        ('P', 'Produto'),
        ('S', 'Serviço'),
    )
    nm_categoria = models.CharField(
        max_length=150, verbose_name='Nome da Categoria')
    tp_categoria = models.CharField(
        max_length=1, verbose_name='Tipo de Categoria', choices=STATUS_CHOICES)
    nm_icone = models.CharField(max_length=20, verbose_name='Nome do Ícone',
                                help_text='Opções no site https://fontawesome.com.')

    def __str__(self):
        return self.nm_categoria

# Produto


class Produto(models.Model):
    STATUS_CHOICES = (
        ('A', 'Ativo'),
        ('I', 'Inativo'),
    )
    usuario = models.ForeignKey(
        User, on_delete=CASCADE, related_name='fk_produto_user1', default=User)
    categoria = models.ForeignKey(
        'Categoria', on_delete=CASCADE, related_name='fk_produto_categoria1')
    nm_produto = models.CharField(
        max_length=150, verbose_name='Nome do Produto')
    dc_produto = models.TextField(verbose_name='Descrição')
    vl_produto = models.FloatField(verbose_name='Valor do Produto')
    dt_cadastro = models.DateTimeField(
        verbose_name='Data do Cadastro', auto_now_add=True)
    st_produto = models.CharField(
        max_length=1, verbose_name='Situação do Produto', choices=STATUS_CHOICES)

    def __str__(self):
        return self.nm_produto

# Condominio


class Condominio(models.Model):
    nm_condominio = models.CharField(
        max_length=150, verbose_name='Nome do Condomínio')
    nm_logradouro = models.CharField(
        max_length=80, verbose_name='Nome do Logradouro')
    nr_logradouro = models.IntegerField(verbose_name='Número', null=True)
    nm_bairro = models.CharField(max_length=45, verbose_name='Bairro')
    tx_complemento = models.CharField(
        max_length=45, verbose_name='Complemento')
    cep = models.CharField(max_length=8, verbose_name='CEP')
    nm_cidade = CharField(max_length=60, verbose_name='Cidade')
    dt_cadastro = DateTimeField(
        verbose_name='Data do Cadastro', auto_now_add=True)

    def __str__(self):
        return self.nm_condominio

# Contato


class Contato(models.Model):
    STATUS_CHOICES = (
        ('Telefone', 'Telefone'),
        ('WhatsApp', 'WhatsApp'),
        ('Telegram', 'Telegram'),
        ('E-Mail', 'E-Mail'),
    )
    condominios = models.ForeignKey(
        'Condominio', on_delete=CASCADE, related_name='fk_contato_condominio1')
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='fk_contato_user1', null=True)
    tp_contato = models.CharField(
        max_length=45, verbose_name='Tipo de Contato', choices=STATUS_CHOICES)
    tx_contato = models.CharField(
        max_length=80, verbose_name='Contato')


# Residencia


class Residencia(models.Model):
    STATUS_CHOICES = (
        ('Telefone', 'Telefone'),
        ('WhatsApp', 'WhatsApp'),
        ('Telegram', 'Telegram'),
        ('E-Mail', 'E-Mail'),
    )
    condominios = models.ForeignKey(
        'Condominio', on_delete=CASCADE, related_name='fk_residencia_condominio1')
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='fk_residencia_user1')
    nm_bloco = models.CharField(
        max_length=45, verbose_name='Nome do Bloco', help_text='Nome do prédio. Ex.: Torre 1, Bloco B, Bloco Camélia.')
    nr_residencia = models.IntegerField(
        verbose_name='Número', choices=STATUS_CHOICES)
