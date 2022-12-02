from django.views import View
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


from .models import Tipo_bodeguero

# Create your views here.
#Se crearan en CBV
'''
NOTA: A la hora de entrar a la url de la api que contiene la view de la clase se puede apreciar un error
llamado: "Object of type QuerySet isn't JSON serializable" Se soluciona cambiando el metodo all por values y convirtiendo la variable
tipos_bodeguero a una lista.

jd = json data, es una variable que carga los datos de la request hacia el body de la appweb

https://www.youtube.com/watch?v=hL52_nB5QSw QUEDE EN EL MINUTO 34:19

PARA ENTRAR A LA VENV DEBO USAR LA BASH DE GIT Y USAR EL SIGUIENTE COMANDO:
source env/Scripts/activate desde la carpeta Proyecto_API

TODO: HACER LA ELIMINACION DE TIPO CARGO Y SEGUIR CON LOS DEMAS MODELOS PARA TRABAJAR EN LA WEB. PARA ESO
DEBO MODIFICAR EL URLS.py dentro de la carpeta api segun lo que requiera
'''

class Tipo_bodeguero_view(View):
    #Se requiere del csrf para poder ingresar datos, sin el, no se podra.
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if (id > 0):
            tipos_bodeguero = list(Tipo_bodeguero.objects.filter(idTipo_bodeguero = id).values())
            if len(tipos_bodeguero) > 0:
                tipo_bodeguero = tipos_bodeguero[0]
            datos = {'mensaje': "Tipo de bodeguero encontrado!", 'tipo_bodeguero': tipo_bodeguero} if len(tipos_bodeguero) > 0 else {'mensaje': "Tipo de bodeguero no encontrado."}
            return JsonResponse(datos)
        else:
            tipos_bodeguero = list(Tipo_bodeguero.objects.values())
            datos = {'mensaje':"exitoso",'tipos_bodeguero':tipos_bodeguero} if len(tipos_bodeguero) > 0 else {'mensaje':"Tipos de bodeguero no encontrados."}
            return JsonResponse(datos)


        

    def post(self, request):
        jd = json.loads(request.body)
        Tipo_bodeguero.objects.create(nombre_cargo = jd['nombre_cargo'])
        datos = {'mensaje':'Datos ingresados exitosamente!'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        tipos_bodeguero = list(Tipo_bodeguero.objects.filter(idTipo_bodeguero = id).values())
        if len(tipos_bodeguero) > 0:
            tipo_bodeguero = Tipo_bodeguero.objects.get(idTipo_bodeguero = id)
            tipo_bodeguero.nombre_cargo = jd['nombre_cargo']
            tipo_bodeguero.save()
            datos = {'mensaje': "Datos actualizados exitosamente!"}
        else:
            datos = {'mensaje': "Tipo de cargo no encontrado."}
        return JsonResponse(datos)

    def delete(self, request):
        pass
