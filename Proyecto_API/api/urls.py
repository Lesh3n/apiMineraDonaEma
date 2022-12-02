from django.urls import path
from .views import Tipo_bodeguero_view

'''
Aqui se declaran las vistas de los modelos para poder tanto ingresar datos, actualizarlos, obtenerlos y borrarlos.
Se debe de hacer con cada funcion o objeto dependiendo de lo que se utilice para hacer que la api funcione.

En este caso, estoy trabajando con CBV (Class based view) pero tambien funciona con FBV (Function based view)
'''

urlpatterns = [
    path('tipoBodeguero/', Tipo_bodeguero_view.as_view(), name='listado_tipo_bodeguero'),
    path('tipoBodeguero/<int:id>', Tipo_bodeguero_view.as_view(), name='buscar_id_tipo_bodeguero')
]