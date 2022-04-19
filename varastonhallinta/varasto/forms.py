from django import forms

from django.contrib.auth.models import User
from varasto.models import Varastotapahtuma #, Varasto, Tuoteryhma, Tuote

# Varastotapahtuma modelista tehty formi uusi_lainaus -sivulle
class UusiLainaus(forms.ModelForm):
    class Meta:
        model = Varastotapahtuma
        fields = [
        "asiakas", 
        "varasto","tuote", "maara", 
        "palautuspaiva"]

# Käyttäjätietojen muokkaus-formi
'''
class MuutaKayttajaa(forms.ModelForm):
    username = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email']
'''
'''
class MuutaProfiilia(forms.ModelForm):
    #kuva = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    #kuva = forms.ImageField()
    class Meta:
        model = Profiili
        fields = ['kuva']
'''