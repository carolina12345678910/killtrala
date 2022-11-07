from django.contrib import admin
from articulos.models import Entrada
from articulos.models import Tinturas
from articulos.models import Diseños_varios
from articulos.models import Convenciones
from articulos.models import Estudio



# Register your models here.
admin.site.register(Entrada)
admin.site.register(Tinturas)
admin.site.register(Diseños_varios)
admin.site.register(Convenciones)
admin.site.register(Estudio)

