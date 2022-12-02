from django.contrib import admin
from .models import Tipo_bodeguero, Usuario, Tipo_objeto, Objeto, Historico

# Register your models here.
admin.site.register(Tipo_bodeguero)
admin.site.register(Usuario)
admin.site.register(Tipo_objeto)
admin.site.register(Objeto)
admin.site.register(Historico)