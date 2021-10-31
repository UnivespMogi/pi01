from django.contrib import admin
from .models import Categoria, Produto, Condominio, Residencia, Contato

# Categoria
admin.site.register(Categoria)

# Produto
admin.site.register(Produto)

# Condomínio
admin.site.register(Condominio)

# Contato
admin.site.register(Contato)

# Residência
admin.site.register(Residencia)
