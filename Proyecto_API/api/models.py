from django.db import models

# Create your models here.
class Tipo_bodeguero(models.Model):
    idTipo_bodeguero = models.AutoField(primary_key=True, blank=False)
    nombre_cargo = models.CharField(max_length=60, blank=False, unique=True)


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre_propietario = models.CharField(max_length=80, blank=False, unique=False)
    apellido_propietario = models.CharField(max_length=80, blank=False, unique=False)
    usuario = models.CharField(max_length=80, blank=False, unique=True)
    contrasena = models.CharField(max_length=60, blank=False, unique=True)
    idTipo_bodeguero = models.ForeignKey(Tipo_bodeguero, on_delete=models.CASCADE)


class Tipo_objeto(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=60, blank=False, unique=True)


class Objeto(models.Model):
    idObjeto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45,blank=False, unique=True)
    cantidad = models.IntegerField(blank=False)
    descripcion = models.TextField(blank=True)
    prestatario = models.CharField(max_length=100,blank=True)
    id_tipo = models.ForeignKey(Tipo_objeto, on_delete=models.CASCADE)



class Historico(models.Model):
    idHistorico = models.AutoField(primary_key=True)
    detalle = models.TextField(blank=True)
    accion = models.CharField(max_length=20,blank=False)
    modificado_por = models.CharField(max_length=80,blank=False)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idObjeto = models.ForeignKey(Objeto, on_delete=models.CASCADE)
