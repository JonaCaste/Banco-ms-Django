# agregamos configs para el admin


from django.contrib import admin
from .models import PQR, PersonaSoporte

# agregamos las tablas a admin para poder administrarse desde allí
admin.site.register(PQR)
admin.site.register(PersonaSoporte)

# Register your models here.
