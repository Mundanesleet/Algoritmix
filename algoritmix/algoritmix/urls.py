from django.contrib import admin
from django.urls import path
from coding_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Página principal

    # Cursos
    path('curso1/', views.curso1, name='curso1'),  # Python Basic
    path('curso2/', views.curso2, name='curso2'),  # Python Pro
    path('curso3/', views.curso3, name='curso3'),  # Scratch

    # Lecciones para Python Basic, Pro, y Scratch
    path('leccion/<int:modulo>/<int:leccion>/', views.ver_leccion, name='ver_leccion'),

    # Ruta para ejecutar código
    path('ejecutar_codigo/', views.ejecutar_codigo, name='ejecutar_codigo'),
]
