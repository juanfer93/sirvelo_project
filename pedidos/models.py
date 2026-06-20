from django.db import models

# 1. USUARIOS
class Usuario(models.Model):
    PERFIL_CHOICES = [('administrador', 'Administrador'), ('usuario', 'Usuario')]
    ESTADO_CHOICES = [('activo', 'Activo'), ('bloqueado', 'Bloqueado')]
    
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True) # unique=True para evitar duplicados 
    contrasena = models.CharField(max_length=128)
    tipo_perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')

    class Meta:
        db_table = 'usuarios' # Fija el nombre de la tabla 

    def __str__(self):
        return f"{self.nombre} ({self.tipo_perfil})"

# 2. CATEGORIA_PRODUCTO
class CategoriaProducto(models.Model):
    ESTADO_CHOICES = [('activo', 'Activo'), ('inactivo', 'Inactivo')]
    
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    imagen_icono = models.CharField(max_length=255, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activo')

    class Meta:
        db_table = 'categoria_producto'

    def __str__(self):
        return self.nombre

# 3. PRODUCTO_MENU
class ProductoMenu(models.Model):
    DISP_CHOICES = [('disponible', 'Disponible'), ('agotado', 'Agotado')]
    
    # Relación uno-a-muchos: una categoría tiene muchos productos 
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_referente = models.CharField(max_length=255, blank=True)
    disponibilidad = models.CharField(max_length=15, choices=DISP_CHOICES, default='disponible')

    class Meta:
        db_table = 'producto_menu'

    def __str__(self):
        return self.nombre

# 4. METODO_PAGO
class MetodoPago(models.Model):
    TIPO_CHOICES = [('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta'), ('transferencia', 'Transferencia')]
    ESTADO_CHOICES = [('activo', 'Activo'), ('inactivo', 'Inactivo')]
    
    nombre = models.CharField(max_length=50)
    tipo_pago = models.CharField(max_length=20, choices=TIPO_CHOICES)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activo')

    class Meta:
        db_table = 'metodo_pago'

    def __str__(self):
        return self.nombre

# 5. PEDIDO
class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('nuevo', 'Nuevo'), 
        ('en preparacion', 'En Preparación'), 
        ('entregado', 'Entregado'), 
        ('rechazado', 'Rechazado')
    ]
    
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT) # Protege integridad 
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.PROTECT)
    fecha_hora = models.DateTimeField(auto_now_add=True) # Fecha automática al crear 
    total_pagar = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='nuevo')
    tipo_entrega = models.CharField(max_length=255)

    class Meta:
        db_table = 'pedido'

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.nombre}"

# 6. DETALLE_PEDIDO
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(ProductoMenu, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'detalle_pedido'

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
