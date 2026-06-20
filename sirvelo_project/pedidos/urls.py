from django.urls import path
from . import views # Importa las vistas de tu app 

urlpatterns = [
    path('', views.listar_pedidos, name='listar'), # Ruta para listar 
    path('crear/', views.crear_pedido, name='crear'), # Ruta para crear 
    path('editar/<int:pedido_id>/', views.editar_pedido, name='editar'), # Captura el ID para editar 
    path('eliminar/<int:pedido_id>/', views.eliminar_pedido, name='eliminar'), # Captura el ID para eliminar 
]