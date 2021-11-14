from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from anuncios.models import Contato
from .forms import UserChangeForm, UserCreationForm
from .models import User

class ContatoInline(admin.TabularInline):
    model = Contato
    extra = 3

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    models = User
    inlines = [ContatoInline]

    list_display = ('username', 'email', 'first_name',
                    'last_name', 'id')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'id')

    def get_queryset(self, request):
        # Get the logged in user
        usuario_logado = User.objects.filter(username=request.user)
        # Override the get_queryset method for Admin
        qs = super(UserAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            return qs.filter(username=usuario_logado[0])
        else:
            return qs
