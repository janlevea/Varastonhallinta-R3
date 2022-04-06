from django import forms

class UusiLainaus(forms.Form):
    varastonhoitaja = forms.CharField(label="Varastonhoitaja", max_length=35, required=True)
    asiakas = forms.CharField(label="Asiakas", max_length=35, required=True)
    tuote = forms.CharField(label="Tuote", max_length=35, required=True)
    maara = forms.IntegerField(label="Määrä", required=True) # help_text="Kuinka monta?"
    aikaleima = forms.DateField(label="Aikaleima", required=True)
    palautuspaiva = forms.DateField(label="Palautuspäivä", required=True)
