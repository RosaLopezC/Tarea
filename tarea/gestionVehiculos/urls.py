from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculo/<int:vehiculo_id>/registrar_entrada/', views.registrar_entrada, name='registrar_entrada'),
    path('registro/<int:registro_id>/registrar_salida/', views.registrar_salida, name='registrar_salida'),
    path('registrar_propietario/', views.registrar_propietario, name='registrar_propietario'),
    path('propietario/<int:propietario_id>/registrar_vehiculo/', views.registrar_vehiculo, name='registrar_vehiculo'),
    path('propietario/<int:propietario_id>/vehiculos/', views.listar_vehiculos, name='listar_vehiculos'),
    path('vehiculo/<int:vehiculo_id>/editar/', views.editar_vehiculo, name='editar_vehiculo'),
    path('vehiculo/<int:vehiculo_id>/eliminar/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('registros/', views.listar_registros, name='listar_registros'),
    path('registros/historial/<int:vehiculo_id>/', views.historial_registro, name='historial_registro'),


]
