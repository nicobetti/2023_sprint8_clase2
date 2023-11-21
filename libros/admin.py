from django.contrib import admin

# Register your models here.

#importamos el modelo Libro definido en el archivo Model
from .models import Libro

# Register your models here.

#Con esta clase ampliamos la configuracion del administrador, extendiendo nuesrta clase propia
#Le decimos que los campos created y updated son de solo lectura
class LibroAdmin (admin.ModelAdmin):
    readonly_fields= ('created-at','updated-at')

#Con esta instruccion registramos Project para que pueda ser gestionado en el admin
admin.site.register(Libro)