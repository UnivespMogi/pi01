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
