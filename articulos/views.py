from django.shortcuts import render
from .models import Entrada
from .models import Tinturas
from .models import Diseños_varios
from .models import Convenciones
from .models import Estudio
from .models import Tatuadores
from .models import Adicional


# Create your views here.
def pagina(request):
	principio = Entrada.objects.all()
	tinturas = Tinturas.objects.all()
	diseñosvarios = Diseños_varios.objects.all()
	convenciones = Convenciones.objects.all()
	estudio = Estudio.objects.all()
	tatuadores = Tatuadores.objects.all()
	adicional = Adicional.objects.all()
	return render(request, 'inicio.html', {'principio':principio,'diseñosvarios':diseñosvarios,'tinturas':tinturas,
		'convenciones':convenciones,'estudio':estudio,'tatuadores':tatuadores,'adicional':adicional})