import json
import subprocess
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
from .models import Modulo, Leccion

# Datos ficticios para los alumnos y lecciones
alumno_info = {
    'balance': 100,
    'lecciones_disponibles': 5
}

contenidoLecciones = {
    (1, 1): 'Esta es la introducción a la programación en Python...',
    (1, 2): 'En esta lección aprenderás sobre las variables en Python...',
    (1, 3): 'Lección: Variables y Tipos de Datos. En programación, una variable es como una "caja" que guarda información.',
    (2, 1): 'Introducción al Módulo 2...',
    # Añade más lecciones según tu necesidad
}

# View para la página principal (Home)
def home(request):
    # Muestra el balance y las lecciones disponibles del alumno
    return render(request, 'home.html', {'alumno': alumno_info})

# View para los cursos individuales
def curso1(request):
    return render(request, 'curso1.html')

def curso2(request):
    return render(request, 'curso2.html')

def curso3(request):
    return render(request, 'curso3.html')

# View para cargar una lección específica
def ver_leccion(request, modulo, leccion):
    # Buscar el módulo y la lección correspondiente
    modulo_obj = get_object_or_404(Modulo, numero=modulo)
    leccion_obj = get_object_or_404(Leccion, modulo=modulo_obj, orden=leccion)

    context = {
        'modulo': modulo_obj,
        'leccion': leccion_obj,
    }
    
    return render(request, 'lecciones/leccion.html', context)

# View para ejecutar el código desde el editor
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
                timeout=10  # Limitar el tiempo de ejecución a 10 segundos
            )

            # Capturar tanto stdout como stderr
            salida = resultado.stdout if resultado.returncode == 0 else resultado.stderr

            return JsonResponse({'resultado': salida})

        except subprocess.TimeoutExpired:
            return JsonResponse({'error': 'El tiempo de ejecución del código ha excedido el límite.'}, status=500)
        except subprocess.CalledProcessError as e:
            return JsonResponse({'error': str(e)}, status=500)
