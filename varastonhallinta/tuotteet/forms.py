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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['tuoteryhma'].widget.attrs.update({'class': 'roundedborder rasekoredborder'})
        self.fields['nimike'].widget.attrs.update({'class': 'roundedborder rasekoredborder'})
        self.fields['maara'].widget.attrs.update({'class': 'roundedborder rasekoredborder bottom-marg'})
        self.fields['hankintapaikka'].widget.attrs.update({'class': 'roundedborder rasekoblueborder'})
        self.fields['kustannuspaikka'].widget.attrs.update({'class': 'roundedborder rasekoblueborder bottom-marg'})
        self.fields['viivakoodi_string'].widget.attrs.update({'class': 'roundedborder blackborder'})