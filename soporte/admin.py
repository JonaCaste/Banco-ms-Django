# agregamos configs para el admin


from django.contrib import admin
from .models import PQR, PersonaSoporte, Bank

# agregamos las tablas a admin para poder administrarse desde allí
admin.site.register(PQR)
admin.site.register(PersonaSoporte)
admin.site.register(Bank)

# Register your models here.
