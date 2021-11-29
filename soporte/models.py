# modelos de la app

# Todo lo relacionado con db va en los modelos


from django.db import models

from django.contrib.auth.models import User  #modelo para la relacion muchos a muchos

# Create your models here.


# nombre de la db = a la tabla
class PersonaSoporte(models.Model):

    # relacion uno a uno, para agregar info extra a User
    # dos tablas uno a uno, una funciona con django y la otra tiene la info extra
    # simulamos un usuario normal, con campos extra de vendedor
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="soporte")
    # PersonaSoporte esta unido con usuario
    # related_name -> Usuario se une a Soporte

    # crear columnas
    ## id por defecto
    nombre = models.CharField(max_length=64)
    edad = models.IntegerField(null=True, blank=True)
    activo = models.BooleanField(default=True)


class PQR(models.Model):

    persona_soporte = models.ForeignKey(PersonaSoporte, on_delete=models.SET_NULL, null=True)
    #on_delete -> define lo que deberia pasar cuando se borra un registro de la relacion
        ## cuando se elimina un registro padre pase esto:
        ## SET_NULL -> cambia el id a null
        ## CASCADE -> elimina en cascada los registros de los registros hijas

    estado = models.CharField(max_length=32)
    comentario = models.TextField(blank=True)
    creacion = models.DateField()

# como hacer una relacion muchos a muchos 
class Bank(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    users = models.ManyToManyField(User)

    #migrar de nuevo
