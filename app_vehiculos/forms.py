from django import forms

class CamionetaFormulario(forms.Form):
    marca = forms.CharField(required=True, max_length=64)
    modelo = forms.CharField(required=True, max_length=256)
    fabricacion = forms.IntegerField(required=True, max_value=80000) 
    cv= forms.IntegerField(max_value=80000) 
    peso= forms.IntegerField(max_value=80000)
    
class AutomovilFormulario(forms.Form):
    marca = forms.CharField(required=True, max_length=64)
    modelo = forms.CharField(required=True, max_length=256) 
    fabricacion = forms.IntegerField(required=True, max_value=80000) 
    cv= forms.IntegerField(max_value=80000) 
    peso= forms.IntegerField(max_value=80000)
    
class MotocicletaFormulario(forms.Form):
    marca = forms.CharField(required=True, max_length=64)
    modelo = forms.CharField(required=True, max_length=256)  
    fabricacion = forms.IntegerField(required=True, max_value=80000) 
    cv= forms.IntegerField(max_value=80000) 
    peso= forms.IntegerField(max_value=80000)