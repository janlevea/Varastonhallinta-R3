from django import forms

from varastonhallinta.tuotteet.models import Tuote

class LisaaTuote(forms.ModelForm):
    class Meta:
        model = Tuote
        fields = [
            "tuoteryhma",
            "nimike", "maara",
            "hankintapaikka", "kustannuspaikka",
            "tuotekuva", "viivakoodi_string", "viivakoodi_img",
        ]