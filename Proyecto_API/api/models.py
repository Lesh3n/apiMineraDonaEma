'''
from django.db import models

Se importa desde una librería interna de django la función models.

En este script llamado "models.py" se maneja todo lo que es la creación de los modelos u tablas
en la base de datos con cada uno de sus atributos dependiendo de cuáles se hayan establecido antes de 
crear la aplicación web en cuestión.


++++ RESTRICCIONES ++++

Cada una de estas variables viene con un models."TipoCampo" y dentro de estas variables vienen sus restricciones
u propiedades, pongamos del siguiente ejemplo:

nombre_vehiculo = models.TipoCampo(restriccion_1 = <valor>, restriccion_2 = <valor>,)

En este caso, se pondrán las restricciones antes de documentar para qué es cada variable y así, evitar
duplicar la explicación.

primary_key = Bool ----> Propiedad que especifica si este valor o campo es primary key o no.
En valor, pueden ir SOLO BOOLEANOS, osea, True o False.

blank = Bool ----> Propiedad que especifica si este campo puede quedar NULL o no.

unique = Bool ----> Propiedad que define si es que el campo es ÚNICO o no.

maxLenght = int ----> Propiedad que define el largo del texto que será recibido en la columna
de la tabla en la base de datos. Esta propiedad, solo se puede utilizar en datos del tipo Char, varchar y TEXT.

on_delete = models.CASCADE ----> Propiedad que va con las claves foráneas de cada campo, esta quiere decir
que si el dato no existe como dato primario en la tabla a la que pertenece, borrará el dato o los datos
que contengan esa clave foránea que ha desaparecido.

'''


from django.db import models

# Create your models here.
'''
class Tipo_bodeguero(models.Model)

Clase que permite la creación de la tabla "Tipo_bodeguero" en la base de datos MySQL.

************ VARIABLES *************

idTipo_bodeguero es una variable AUTOINCREMENTABLE, es la ID del tipo de bodeguero y además
esta es primary key.

Como única restricción tiene que esta NO se puede dejar en blanco.
'''
class Tipo_bodeguero(models.Model):
    idTipo_bodeguero = models.AutoField(primary_key=True, blank=False)
    nombre_cargo = models.CharField(max_length=60, blank=False, unique=True)

'''
class Usuario(models.Model) 

Es una clase que permite la creación de la tabla "Usuario", en la cuál, se contendrán los datos
de cada usuario pertenenciente a cada uno de los trabajadores de la bodega.


VARIABLES 


idUsuario ---> Variable del tipo AI y la cuál a su vez es una primary key que crea una columna de un tipo de dato
INT. Esta columna se encargará de guardad las ID's de las cuentas de usuario.

nombre_propietario ---> Variable que guarda un dato del tipo varchar con restricciones como el largo
máximo de carácteres que esta columna puede soportar, blank=False indica que NO se puede dejar en blanco.
Y unique=False indica que esta variable no es del tipo ÚNICO, aunque Django hace esto por defecto siempre es
mejor establecerlo uno mismo, solo por seguridad.

apellido_propietario ---> Variable que crea una columna con un tipo de dato VARCHAR, en este caso, esta variable
guarda el apellido del propietario de la cuenta.

nombre_usuario ---> Variable que crea una columna con un tipo de dato VARCHAR, en este caso, esta variable
guarda el nombre de usuario de la cuenta.

contrasena ---> Variable que crea una columna con un tipo de dato VARCHAR, en este caso, esta variable
guarda la contraseña de la cuenta.

idTipo_bodeguero = Variable que crea una columna que almacena una ForeignKey que viene desde Tipo_bodeguero

'''
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre_propietario = models.CharField(max_length=80, blank=False, unique=False)
    apellido_propietario = models.CharField(max_length=80, blank=False, unique=False)
    nombre_usuario = models.CharField(max_length=80, blank=False, unique=True)
    contrasena = models.CharField(max_length=60, blank=False, unique=True)
    idTipo_bodeguero = models.ForeignKey(Tipo_bodeguero, on_delete=models.CASCADE, blank=False, null=True)

'''
class Tipo_objeto(models.Model) ----> Objeto que permite la creación de la tabla Tipo_Objeto

------ Variables ------

id_tipo ----> Crea una columna que almacena la ID del tipo de objeto. Esta columna es AI y PK.

nombre_tipo  ----> Crea una columna que almacena el nombre del tipo de objeto.

'''


class Tipo_objeto(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=60, blank=False, unique=True)

'''
class Tipo_objeto(models.Model) ----> Objeto que permite la creación de la tabla Tipo_Objeto

------ Variables ------

idObjeto ----> Crea una columna que almacena la ID del tipo de objeto. Esta columna es AI y PK.

nombre  ----> Crea una columna que almacena el nombre del objeto.

cantidad  ----> Crea una columna que almacena la cantidad del objeto.

descripcion  ----> Crea una columna que almacena la descripción del objeto.

prestatario  ----> Crea una columna que almacena el nombre del prestatario.

id_tipo  ----> Crea una columna que almacena la ID del tipo de objeto, esto, obteniéndose como 
clave foránea

'''


class Objeto(models.Model):
    idObjeto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45,blank=False, unique=True)
    cantidad = models.IntegerField(blank=False)
    descripcion = models.TextField(blank=True)
    prestatario = models.CharField(max_length=100,blank=True)
    id_tipo = models.ForeignKey(Tipo_objeto, on_delete=models.CASCADE)


'''
class Histórico(models.Model) ----> Objeto que permite la creación de la tabla Histórico

------ Variables ------

idHistorico ----> Crea una columna que almacena la ID del histórico. Esta columna es AI y PK.

detalle  ----> Crea una columna que almacena el detalle de lo cambiado en el histórico.

accion  ----> Crea una columna que almacena el tipo de acción que fue realizada en esa tabla.

modificado_por  ----> Crea una columna que almacena el nombre de usuario de la persona que modificó dicho dato.

idUsuario  ----> Crea una columna que almacena el id del usuario que modificó dicho dato.

idObjeto  ----> Crea una columna que almacena el id del objeto que fue removido, actualizado o creado.

'''



class Historico(models.Model):
    idHistorico = models.AutoField(primary_key=True)
    detalle = models.TextField(blank=True)
    accion = models.CharField(max_length=20,blank=False)
    modificado_por = models.CharField(max_length=80,blank=False)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idObjeto = models.ForeignKey(Objeto, on_delete=models.CASCADE)