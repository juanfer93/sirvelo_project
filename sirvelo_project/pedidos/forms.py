from django import forms
from pedidos.models import MetodoPago, Pedido, Usuario

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        # Aquí defines qué campos verá el usuario en la interfaz
        fields = ['usuario', 'metodo_pago', 'tipo_entrega', 'estado']

        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'metodo_pago': forms.Select(attrs={'class': 'form-control'}),
            'tipo_entrega': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'usuario': 'Cliente / Mesero',
            'metodo_pago': 'Forma de Pago',
            'tipo_entrega': 'Lugar de entrega',
            'estado': 'Estado del Pedido',
        }


class MeseroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'contrasena', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'contrasena': forms.PasswordInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }


class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = ['nombre', 'tipo_pago', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_pago': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
