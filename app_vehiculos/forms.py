from django import forms

class VehiculosFormulario(forms.Form):
    marca = forms.CharField(required=True, max_length=64)
    modelo = forms.CharField(max_length=256)
    comision = forms.IntegerField(required=True, max_value=80000)    
    fabricacion = forms.IntegerField(required=True, max_value=80000) 
    cv= forms.IntegerField(required=True, max_value=80000) 
    peso= forms.IntegerField(required=True, max_value=80000)