from django.contrib import admin
from .models import Usuario, UnidadeOrganizacional, UsuarioSSH

admin.site.register(Usuario)
admin.site.register(UsuarioSSH)
admin.site.register(UnidadeOrganizacional)