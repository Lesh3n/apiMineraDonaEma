'''
Desde django.apps se hace la importación de AppConfig, una librería interna de Django,
que permite la configuración de una aplicación en un proyecto de Django.
'''
from django.apps import AppConfig


'''
Se crea la configuración interna de cada una de las tablas que poblará django en la base de datos.
Esto, poniendo un prefijo a cada tabla antes de crearla.
'''
class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    '''
    name = 'api'
    
    Hace que cada tabla creada empiece con el prefijo "api"

    Por EJ: api.objeto o api.usuario
    '''
    name = 'api'
