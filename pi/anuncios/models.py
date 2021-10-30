from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Categoria(models.Model):
    STATUS_CHOICES = (
        ('P', 'Produto'),
        ('S', 'Serviço'),
    )
    nm_categoria = models.CharField(max_length=150, verbose_name='Nome da Categoria')
    tp_categoria = models.CharField(max_length=1, verbose_name='Tipo de Categoria', choices=STATUS_CHOICES)
    nm_icone = models.CharField(max_length=20, verbose_name='Nome do Ícone', help_text='Opções no site https://fontawesome.com.')

    def __str__(self):
        return self.nm_categoria

class Produto(models.Model):
    STATUS_CHOICES = (
        ('A', 'Ativo'),
        ('I', 'Inativo'),
    )
    usuario = models.ForeignKey(User, on_delete=CASCADE, related_name='fk_produto_user1', default=User)
    categoria = models.ForeignKey('Categoria', on_delete=CASCADE, related_name='fk_produto_categoria1')
    nm_produto = models.CharField(max_length=150, verbose_name='Nome do Produto')
    dc_produto = models.TextField(verbose_name='Descrição')
    vl_produto = models.FloatField(verbose_name='Valor do Produto')
    dt_cadastro = models.DateTimeField(verbose_name='Data do Cadastro', auto_now_add=True)
    st_produto = models.CharField(max_length=1, verbose_name='Situação do Produto', choices=STATUS_CHOICES)

    def __str__(self):
        return self.nm_produto
