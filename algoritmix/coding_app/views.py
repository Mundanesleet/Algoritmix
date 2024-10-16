import json
import subprocess
import sys
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from django.http import HttpResponse

def home(request):
    alumno = {
        'balance': 100,
        'lecciones_disponibles': 5
    }
    return render(request,'home.html', {'alumno': alumno})

def curso1(request):
    return render(request, 'curso1.html')

def curso2(request):
    return render(request, 'curso2.html')

def curso3(request):
    return render(request, 'curso3.html')

# Lecciones para python basic

# Datos de ejemplo para las lecciones
contenidoLecciones = {
    (1, 1): 'Esta es la introducción a la programación en Python...',
    (1, 2): 'En esta lección aprenderás sobre las variables en Python...',
    (2, 1): 'Introducción al Módulo 2...',
    # Añade más lecciones aquí
}

def leccion_detalle(request, modulo, leccion):
    contenido = contenidoLecciones.get((modulo, leccion), 'Contenido no disponible')
    return render(request, 'leccion.html', {'modulo': modulo, 'leccion': leccion, 'contenido': contenido})

@csrf_exempt
def ejecutar_codigo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            codigo = data.get('codigo')

            if not codigo:
                return JsonResponse({'error': 'No se recibió código para ejecutar'}, status=400)

            # Ejecutar el código usando subprocess
            resultado = subprocess.run(
                ['python3', '-c', codigo],
                text=True,
                capture_output=True,
                timeout=10
            )

            return JsonResponse({'resultado': resultado.stdout})

        except subprocess.CalledProcessError as e:
            return JsonResponse({'error': str(e)}, status=500)