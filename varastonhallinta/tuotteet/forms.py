from django import forms

from tuotteet.models import Tuote, Tuoteryhma

class LisaaTuote(forms.ModelForm):
    class Meta:
        model = Tuote
        fields = [
            "tuoteryhma",
            "nimike", "maara",
            "hankintapaikka", "kustannuspaikka",
            "viivakoodi_plaintxt"
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['tuoteryhma'].widget.attrs.update({'class': 'roundedborder rasekoredborder'})
        self.fields['nimike'].widget.attrs.update({'class': 'roundedborder rasekoredborder'})
        self.fields['maara'].widget.attrs.update({'class': 'roundedborder rasekoredborder bottom-marg'})
        self.fields['hankintapaikka'].widget.attrs.update({'class': 'roundedborder rasekoblueborder'})
        self.fields['kustannuspaikka'].widget.attrs.update({'class': 'roundedborder rasekoblueborder bottom-marg'})
        self.fields['viivakoodi_plaintxt'].widget.attrs.update({'class': 'roundedborder blackborder'})

class LisaaRyhma(forms.ModelForm):
    class Meta:
        model = Tuoteryhma
        fields = [
            "nimi"
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['nimi'].label = "Tuoteryhmän nimi"
        self.fields['nimi'].widget.attrs.update({'class': 'roundedborder rasekoredborder'})

# class MuutaTuotetta(forms.ModelForm):
#     class Meta:
#         model = Tuote
#         fields = [
#             "tuoteryhma", "nimike", "maara",
#             "hankintapaikka", "kustannuspaikka",
#             "tuotekuva", "viivakoodi_plaintxt"
#         ]