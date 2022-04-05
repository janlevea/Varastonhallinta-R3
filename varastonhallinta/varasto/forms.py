'''
from django import forms

# WIP
class UusiLainaus(forms.form):
    varastonhoitaja = forms.CharField(max_length=200)
    lainaaja = forms.CharField(max_length=200)
    tuote = forms.CharField(max_length=200)
    maara = forms.IntegerField(help_text="Kuinka monta?")
'''