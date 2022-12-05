'''
En este archivo "admin.py" se despliega la información que el apartado de admin necesita, para que,
en caso de que un administrador relacionado a la compañía lo necesite, pueda ingresar datos o revisar registros
sin necesidad de acceder al programa per-se.

'''


from django.contrib import admin
'''
Se importan los modelos Tipo_bodeguero, Usuario, Tipo_objeto, Objeto y Histórico para que estos puedan
ser desplegados en el panel de control de administrador que posee Django. Estos modelos, se importan tanto
como para inserciones, actualizaciones, vista de los datos y borrado de los mismos. 

Cada uno de éstos modelos posee sus propios atributos pertenecientes a cada tabla en la base de datos.
'''
from .models import Tipo_bodeguero, Usuario, Tipo_objeto, Objeto, Historico

'''
Se registran los modelos anteriormente mencionados a la interfaz de djangoAdmin. Esto, con el fin de que
aparezcan en el panel de control de administrador que posee Django por default.
'''
# Register your models here.
admin.site.register(Tipo_bodeguero)
admin.site.register(Usuario)
admin.site.register(Tipo_objeto)
admin.site.register(Objeto)
admin.site.register(Historico)