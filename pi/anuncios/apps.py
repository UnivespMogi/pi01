from django.apps import AppConfig
from django import forms


class AnunciosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'anuncios'


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


#status = forms.ChoiceField(choices = STATUS_CHOICES, label="", initial='', widget=forms.Select(), required=True)