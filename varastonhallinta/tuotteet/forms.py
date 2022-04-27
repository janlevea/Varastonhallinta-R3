from django import forms

from tuotteet.models import Tuote

class LisaaTuote(forms.ModelForm):
    class Meta:
        model = Tuote
        fields = [
            "tuoteryhma",
            "nimike", "maara",
            "hankintapaikka", "kustannuspaikka",
            "viivakoodi_string"
        ]