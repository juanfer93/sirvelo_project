from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from pedidos.models import MetodoPago, Pedido, Usuario
from .forms import MeseroForm, MetodoPagoForm, PedidoForm

# 1. LISTAR PEDIDOS CON PAGINACIÓN
def listar_pedidos(request):
    # Se obtienen todos los registros de la tabla pedido
    pedidos_list = Pedido.objects.all().order_by('-fecha_hora')
    
    # Configuración de la paginación a 10 registros por página
    paginator = Paginator(pedidos_list, 10) 
    page_number = request.GET.get('page')
    pedidos = paginator.get_page(page_number)
    
    # Se renderiza la plantilla de listado enviando los objetos paginados
    return render(request, 'pedidos/listar.html', {'pedidos': pedidos})

# 2. CREAR UN NUEVO PEDIDO
def crear_pedido(request):
    if request.method == 'POST':
        # Si la petición es POST, se procesan los datos del formulario
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save() # Guarda en la base de datos MySQL
            return redirect('pedidos:listar') # Redirige al listado tras el éxito
    else:
        # Si es GET, se muestra el formulario vacío 
        form = PedidoForm()
    
    return render(request, 'pedidos/formulario.html', {'form': form})

# 3. EDITAR UN PEDIDO EXISTENTE
def editar_pedido(request, pedido_id):
    # Se busca el pedido por su ID o se devuelve un error 404 limpio
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    
    if request.method == 'POST':
        # Se vincula el formulario a la instancia del pedido encontrado
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('pedidos:listar')
    else:
        # Se carga el formulario con los datos actuales del pedido
        form = PedidoForm(instance=pedido)
    
    return render(request, 'pedidos/formulario.html', {'form': form})

# 4. ELIMINAR UN PEDIDO
def eliminar_pedido(request, pedido_id):
    # Captura el identificador y recupera el objeto
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    
    # Ejecuta la eliminación física en la base de datos
    pedido.delete()
    
    # Regresa automáticamente al listado
    return redirect('pedidos:listar')


def listar_meseros(request):
    meseros = Usuario.objects.filter(tipo_perfil='usuario').order_by('nombre')
    return render(request, 'pedidos/listar_meseros.html', {'meseros': meseros})


def crear_mesero(request):
    if request.method == 'POST':
        form = MeseroForm(request.POST)
        if form.is_valid():
            mesero = form.save(commit=False)
            mesero.tipo_perfil = 'usuario'
            mesero.save()
            return redirect('pedidos:listar_meseros')
    else:
        form = MeseroForm()

    return render(request, 'pedidos/formulario_mesero.html', {'form': form})


def listar_metodos_pago(request):
    metodos_pago = MetodoPago.objects.all().order_by('nombre')
    return render(request, 'pedidos/listar_metodos_pago.html', {'metodos_pago': metodos_pago})


def crear_metodo_pago(request):
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedidos:listar_metodos_pago')
    else:
        form = MetodoPagoForm()

    return render(request, 'pedidos/formulario_metodo_pago.html', {'form': form})
