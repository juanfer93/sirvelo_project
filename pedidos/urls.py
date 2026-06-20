from django.urls import path
from sirvelo_project.pedidos import views

app_name = 'pedidos'

urlpatterns = [
    path('', views.listar_pedidos, name='listar'),
    path('crear/', views.crear_pedido, name='crear'),
    path('editar/<int:pedido_id>/', views.editar_pedido, name='editar'),
    path('eliminar/<int:pedido_id>/', views.eliminar_pedido, name='eliminar'),
    path('meseros/', views.listar_meseros, name='listar_meseros'),
    path('meseros/crear/', views.crear_mesero, name='crear_mesero'),
    path('metodos-pago/', views.listar_metodos_pago, name='listar_metodos_pago'),
    path('metodos-pago/crear/', views.crear_metodo_pago, name='crear_metodo_pago'),
]
