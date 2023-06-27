from django import forms

class NewDepartamento(forms.Form):
    #departamento attributtes
    name = forms.CharField(max_length=50)
    short_name = forms.CharField(max_length=20)
    #empleado attributtes
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

