from django.apps import AppConfig
from django import forms
from .models import Categoria, Produto, Servico, Contato




STATUS_CHOICES = (
        ('Login e Cadastro de usuario', 'Login e Cadastro de usuario'),
        ('Cadastro de produtos/serviço', 'Cadastro de produtos/serviço'),
        ('Criticas e Sugestões', 'Criticas e Sugestões'),
        ('Outros', 'Outros'),
        ('','')
)

class ContactForm(forms.Form):
    nome = forms.CharField(required=True)
    seu_email = forms.EmailField(required=True)
    assunto = forms.ChoiceField(choices = STATUS_CHOICES, label='Assunto', initial='',widget=forms.Select(), required=True)
    mensagem = forms.CharField(widget=forms.Textarea, required=True)




class Produto_Form(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nm_produto', 'categoria','dc_produto','vl_produto','st_produto','imagem')



class Contato_Form(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ('tp_contato','tx_contato')


