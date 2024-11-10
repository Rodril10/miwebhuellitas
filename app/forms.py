from django.forms import ModelForm
from .models import Eventos, Testimonios, Adopta, Dona

class DonaForm(ModelForm):
    class Meta:
        model = Dona
        fields = ['NOMBRE', 'VALOR', 'METODO_PAGO', 'COMENTARIOS' ]
                
        
class TestimoniosForm(ModelForm):
    class Meta:
        model = Testimonios
        fields = ['NOMBRE_APELLIDO', 'ACCION', 'TESTIMONIO']