from django.views import View
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


from .models import Tipo_bodeguero
from .models import Usuario
from .models import Tipo_objeto
from .models import Objeto

# Create your views here.
#Se crearan en CBV
'''
NOTA: A la hora de entrar a la url de la api que contiene la view de la clase se puede apreciar un error
llamado: "Object of type QuerySet isn't JSON serializable" Se soluciona cambiando el metodo all por values y convirtiendo la variable
tipos_bodeguero a una lista.

jd = json data, es una variable que carga los datos de la request hacia el body de la appweb

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



    def delete(self, request, id):
        tipos_bodeguero = list(Tipo_bodeguero.objects.filter(idTipo_bodeguero = id).values())
        if len(tipos_bodeguero) > 0:
            Tipo_bodeguero.objects.filter(idTipo_bodeguero = id).delete()
            datos = {'mensaje':"Tipo bodeguero eliminado exitosamente!"}
        else:
            datos = {'mensaje': "Tipo de cargo no encontrado."}
        return JsonResponse(datos)



class Usuario_view(View):
    #Se requiere del csrf para poder ingresar datos, sin el, no se podra.
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)



    def get(self, request, id = 0):
        if (id > 0):
            usuarios = list(Usuario.objects.filter(idUsuario = id).values())
            if len(usuarios) > 0:
                usuario = usuarios[0]
            datos = {'mensaje': "Usuario encontrado!", 'usuario': usuario} if len(usuarios) > 0 else {'mensaje': "Usuario no encontrado."}
            return JsonResponse(datos)
        else:
            usuarios = list(Usuario.objects.values())
            datos = {'mensaje':"exitoso",'usuarios':usuarios} if len(usuarios) > 0 else {'mensaje':"Usuarios no encontrados."}
            return JsonResponse(datos)


        
    def post(self, request):
        jd = json.loads(request.body)
        Usuario.objects.create(nombre_propietario = jd['nombre_propietario'], apellido_propietario = jd['apellido_propietario'], nombre_usuario = jd['nombre_usuario'], contrasena = jd['contrasena'], idTipo_bodeguero_id = jd['idTipo_bodeguero_id'])
        datos = {'mensaje':'Usuarios ingresados exitosamente!'}
        return JsonResponse(datos)



    def put(self, request, id):
        jd = json.loads(request.body)
        usuarios = list(Usuario.objects.filter(idUsuario = id).values())
        if len(usuarios) > 0:
            usuario = Usuario.objects.get(idUsuario = id)
            usuario.nombre_propietario = jd['nombre_propietario']
            usuario.apellido_propietario = jd['apellido_propietario']
            usuario.nombre_usuario = jd['nombre_usuario']
            usuario.contrasena = jd['contrasena']
            usuario.idTipo_bodeguero_id = jd['idTipo_bodeguero_id']
            usuario.save()
            datos = {'mensaje': "Usuario actualizado exitosamente!"}
        else:
            datos = {'mensaje': "Usuario a editar no encontrado."}
        return JsonResponse(datos)



    def delete(self, request, id):
        usuarios = list(Usuario.objects.filter(idUsuario = id).values())
        if len(usuarios) > 0:
            Usuario.objects.filter(idUsuario = id).delete()
            datos = {'mensaje':"Usuario eliminado exitosamente!"}
        else:
            datos = {'mensaje': "Usuario no encontrado"}
        return JsonResponse(datos)



class Tipo_objeto_view(View):
    #Se requiere del csrf para poder ingresar datos, sin el, no se podra.
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)



    def get(self,request,id = 0):
        if (id > 0):
            tipos_objeto = list(Tipo_objeto.objects.filter(id_tipo = id).values())
            if len(tipos_objeto) > 0:
                tipo_objeto = tipos_objeto[0]
            datos = {'mensaje': "Tipo de objeto encontrado!", 'tipo_objeto': tipo_objeto} if len(tipos_objeto) > 0 else {'mensaje': "Tipo de objeto no encontrado."}
            return JsonResponse(datos)
        else:
            tipos_objeto = list(Tipo_objeto.objects.values())
            datos = {'mensaje':"exitoso",'tipos_objeto':tipos_objeto} if len(tipos_objeto) > 0 else {'mensaje':"Los objetos no existen."}
            return JsonResponse(datos)


        
    def post(self, request):
        jd = json.loads(request.body)
        Tipo_objeto.objects.create(nombre_tipo = jd['nombre_tipo'])
        datos = {'mensaje':'Datos ingresados exitosamente!'}
        return JsonResponse(datos)



    def put(self, request, id):
        jd = json.loads(request.body)
        tipos_objeto = list(Tipo_objeto.objects.filter(id_tipo = id).values())
        if len(tipos_objeto) > 0:
            tipo_objeto = Tipo_objeto.objects.get(id_tipo = id)
            tipo_objeto.nombre_tipo = jd['nombre_tipo']
            tipo_objeto.save()
            datos = {'mensaje': "Datos actualizados exitosamente!"}
        else:
            datos = {'mensaje': "Tipo de objeto no encontrado."}
        return JsonResponse(datos)



    def delete(self, request, id):
        tipos_objeto = list(Tipo_objeto.objects.filter(id_tipo = id).values())
        if len(tipos_objeto) > 0:
            Tipo_objeto.objects.filter(id_tipo = id).delete()
            datos = {'mensaje':"Tipo objeto eliminado exitosamente!"}
        else:
            datos = {'mensaje': "Tipo de cargo no encontrado."}
        return JsonResponse(datos)



class Objeto_view(View):
    #Se requiere del csrf para poder ingresar datos, sin el, no se podra.
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)



    def get(self,request,id = 0):
        if (id > 0):
            objetos = list(Objeto.objects.filter(idObjeto = id).values())
            if len(objetos) > 0:
                tipo_objeto = objetos[0]
            datos = {'mensaje': "Objeto encontrado!", 'objeto': tipo_objeto} if len(objetos) > 0 else {'mensaje': "Objeto no encontrado."}
            return JsonResponse(datos)
        else:
            objetos = list(Objeto.objects.values())
            datos = {'mensaje':"exitoso",'objetos':objetos} if len(objetos) > 0 else {'mensaje':"Los objetos no existen."}
            return JsonResponse(datos)


        
    def post(self, request):
        jd = json.loads(request.body)
        Objeto.objects.create(nombre = jd['nombre'], cantidad = jd['cantidad'], descripcion = jd['descripcion'], prestatario = jd['prestatario'], id_tipo_id = jd['id_tipo_id'])
        datos = {'mensaje':'Datos ingresados exitosamente!'}
        return JsonResponse(datos)



    def put(self, request, id):
        jd = json.loads(request.body)
        objetos = list(Objeto.objects.filter(idObjeto = id).values())
        if len(objetos) > 0:
            objeto = Objeto.objects.get(idObjeto = id)
            objeto.nombre = jd['nombre']
            objeto.cantidad = jd['cantidad']
            objeto.descripcion = jd['descripcion']
            objeto.prestatario = jd['prestatario']
            objeto.id_tipo_id = jd['id_tipo_id']
            objeto.save()
            datos = {'mensaje': "Objeto actualizado exitosamente!"}
        else:
            datos = {'mensaje': "Objeto no encontrado."}
        return JsonResponse(datos)



    def delete(self, request, id):
        objetos = list(Objeto.objects.filter(idObjeto = id).values())
        if len(objetos) > 0:
            Objeto.objects.filter(idObjeto = id).delete()
            datos = {'mensaje':"Objeto eliminado exitosamente!"}
        else:
            datos = {'mensaje': "Objeto no encontrado."}
        return JsonResponse(datos)


