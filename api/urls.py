'''
from django.urls import path

Se importa "path" desde la librería "django.urls".

La función path permite que se puedan manejar rutas y en esas rutas permitir que se almacenen
las vistas provenientes desde views.py
'''
from django.urls import path
'''
from .views import Tipo_bodeguero_view
from .views import Usuario_view
from .views import Tipo_objeto_view
from .views import Objeto_view

Primero se importan las vistas desde el script de python "views.py" los cuáles contienen
cada una de las vistas. Estas vistas, contienen las instrucciones de GET, POST, PUT Y DELETE de la 
api REST.
'''
from .views import Tipo_bodeguero_view
from .views import Usuario_view
from .views import Tipo_objeto_view
from .views import Objeto_view

'''
Aqui se declaran las vistas de los modelos para poder tanto ingresar datos, actualizarlos, obtenerlos y borrarlos.
Se debe de hacer con cada funcion o objeto dependiendo de lo que se utilice para hacer que la api funcione.

En este caso, estoy trabajando con CBV (Class based view) pero tambien funciona con FBV (Function based view)
'''

'''
Este URLS.py va dentro de la aplicación, osea, dentro de la carpeta api.

urlpatters = [] es una variable que contiene una lista que guardará cada uno de los patrones de URL
designados por el programador.

path('url/', vista_view.as_view(), nombre = 'str')

En el segundo parámetro se debe indicar la función de la vista que se utilizará, esta función fue importada
con anterioridad más arriba.
'''
urlpatterns = [
    path('tipoBodeguero/', Tipo_bodeguero_view.as_view(), name='listado_tipo_bodeguero'),
    path('tipoBodeguero/<int:id>', Tipo_bodeguero_view.as_view(), name='buscar_id_tipo_bodeguero'),
    path('usuario/', Usuario_view.as_view(), name='listado_usuarios'),
    path('usuario/<int:id>', Usuario_view.as_view(), name='buscar_id_usuario'),
    path('tipoObjeto/', Tipo_objeto_view.as_view(), name='listado_tipo_objeto'),
    path('tipoObjeto/<int:id>', Tipo_objeto_view.as_view(), name='buscar_id_tipo_objeto'),
    path('objeto/', Objeto_view.as_view(), name='listado_objeto'),
    path('objeto/<int:id>', Objeto_view.as_view(), name='buscar_id_objeto')
]