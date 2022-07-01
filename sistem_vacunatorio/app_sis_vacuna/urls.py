from django.urls import path

from . import views

urlpatterns = [
    #index
    path('index/', views.index, name='index'),
    #ingreso
    path('ingresar_persona/', views.ingresar_persona, name='ingresar_persona'),
    path('ingreso_persona/', views.ingreso_persona),
    #eliminar
    path('eliminar_persona/', views.eliminar_persona),
    path('eliminacion_personas/', views.eliminacion_personas),
    #listar
    path('listar_persona/', views.listar_persona),
    path('listar_todo_persona/', views.listar_todo_persona),
    #busqueda
    path('busqueda_persona/', views.busqueda_persona),
    path('buscar_persona/', views.buscar_persona),
]