from django.contrib import admin
from .models import Categoria, Produto, Condominio, Residencia, Contato, Servico

'''
Classe criada para exibição tabular das informações de contato.
Na área administrativa do Django será apresentada no formulário
Condominío as informações para o cadastro de formas de Contato. Por
exemplo: WhatsApp, Telefone, E-Mail.
'''
class ContatoInline(admin.TabularInline):
    model = Contato
    extra = 3

class CondominioAdmin(admin.ModelAdmin):
    inlines = [ContatoInline]

class ProdutoAdmin(admin.ModelAdmin):
    model = Produto
    # exclude = ('dt_cadastro','usuario')
    list_display = ('categoria', 'nm_produto', 'dc_produto',
                    'vl_produto', 'st_produto')
    #fields = ['categoria', 'nm_produto', 'dc_produto',
              #'vl_produto', 'st_produto']
    # list_filter = ('projeto', 'tipo', 'status')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ProdutoAdmin, self).save_model(request, obj, form, change)


admin.site.register(Condominio, CondominioAdmin)
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Servico)
