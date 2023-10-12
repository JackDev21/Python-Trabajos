from django import forms
from .models import Nomina

class NominaForm(forms.ModelForm):
    class Meta:
        model = Nomina
        fields = '__all__'
