from django import forms
from varasto.models import Varasto, Tuoteryhma, Tuote, Varastotapahtuma

# Modelista tehty formi
class UusiLainaus(forms.ModelForm):
    class Meta:
        model = Varastotapahtuma
        fields = [
        "varastonhoitaja", "asiakas", 
        "varasto",
        "tuote", "maara", "palautuspaiva"]
# TODO: arkistotunnus täytyy luoda lainauksiin
# tällä hetkellä aina tyhjä

# TODO: Koodin kommentointi kaikissa tiedostoissa puutteellinen

# Käsin tehty formi
# class UusiLainaus(forms.Form):
#     varastonhoitaja = forms.CharField(label="Varastonhoitaja", max_length=35, required=True)
#     asiakas = forms.CharField(label="Asiakas", max_length=35, required=True)
#     tuote = forms.CharField(label="Tuote", max_length=35, required=True)
#     maara = forms.IntegerField(label="Määrä", required=True) # help_text="Kuinka monta?"
#     aikaleima = forms.DateField(label="Aikaleima", required=True)
#     palautuspaiva = forms.DateField(label="Palautuspäivä", required=True)