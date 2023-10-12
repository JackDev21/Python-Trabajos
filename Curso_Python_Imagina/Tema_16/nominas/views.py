from django.shortcuts import render, get_object_or_404
from .models import Nomina
from .forms import NominaForm
from django.http import HttpResponse

def nominas(request):
    return HttpResponse("¡Bienvenido a la APP de nominas!")
                       
def inicio(request):
    return render(request, 'inicio.html')

def crear_nomina(request):
   if request.method == 'POST':
      form = NominaForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponse( "¡Nomina creada correctamente!")
         
         
   else:
      form = NominaForm()
   return render(request, 'crear_nomina.html', {'form': form})

def lista(request):
    nominas = Nomina.objects.all()
    return render(request, 'lista.html', {'nominas': nominas})

def detalle_nomina(request, id_nomina):
    nomina = get_object_or_404(Nomina, id=id_nomina)
    return render(request, 'detalle_nomina.html', {'nomina': nomina})
   