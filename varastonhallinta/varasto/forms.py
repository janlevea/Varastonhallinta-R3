from django import forms

from varasto.models import Varastotapahtuma

# Importoi date/time-kirjastot käytettäväksi aikaleimoissa/palautuspäivässä
from datetime import timedelta
from django.utils import timezone

from kayttajat.models import Kayttaja
from tuotteet.models import Tuote

# Varastotapahtuma modelista tehty formi uusi_lainaus -sivulle
class UusiLainaus(forms.ModelForm):
    class Meta:
        model = Varastotapahtuma
        fields = [
            # Tarpeelliset kentät
            "asiakas", 
            "tuote", "maara", 
            "viim_palautuspaiva"
        ]
        widgets = {
            'viim_palautuspaiva': forms.DateInput(
                attrs={'type': 'date'}),
        }

    avoimetTuotteet = Tuote.objects.filter(poistettu = False)
    tuote = forms.ModelChoiceField(queryset=avoimetTuotteet)

    def __init__(self, *args, **kwargs):
        viim_palautuspaiva_initial = timezone.now() + timedelta(days=14) 

        super().__init__(*args, **kwargs)
        # Aseta css-luokkia formin tyylittelyä varten
        self.fields['asiakas'].widget.attrs.update({'class': 'rasekoredborder roundedborder bottom-marg'})
        self.fields['tuote'].widget.attrs.update({'class': 'rasekoblueborder roundedborder'})
        self.fields['maara'].widget.attrs.update({'class': 'rasekoblueborder roundedborder bottom-marg'})
        self.fields['viim_palautuspaiva'].widget.attrs.update(
            {
                'class': 'blackborder roundedborder bottom-marg',
                'value': viim_palautuspaiva_initial.date
            })

def haeLainaajat():
    ### Näytä valinnassa vain ne asiakkaat joilla on avoimia lainauksia:
    avoimetVarastotapahtumat = Varastotapahtuma.objects.filter(avoin = True)
    asiakkaat_idLista = avoimetVarastotapahtumat.values_list("asiakas", flat=True)

    asiakkaat_vain_kerran_idLista = []
    for asiakasId in asiakkaat_idLista:
        if not asiakasId in asiakkaat_vain_kerran_idLista:
            asiakkaat_vain_kerran_idLista.append(asiakasId)
        
    asiakkaat_queryset = Kayttaja.objects.filter(pk__in=asiakkaat_vain_kerran_idLista)
    return asiakkaat_queryset

class PalautaLainaus(forms.ModelForm):
    class Meta:
        model = Varastotapahtuma
        fields = [
            # Etsi lainauksia asiakkaan mukaan
            "asiakas"
        ]

    asiakkaat_queryset = haeLainaajat()
    asiakas = forms.ModelChoiceField(
        queryset=asiakkaat_queryset, 
        label="Asiakkaat joilla avoimia lainauksia:", 
        required=False,
        empty_label="Kaikki")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asiakas'].widget.attrs.update({'class': 'rasekoredborder roundedborder bottom-marg'})
        self.fields['asiakas'].queryset = haeLainaajat() # Päivitä asiakaslista ladattaessa sivu uudelleen

class LainausJarjestys(forms.Form):
    avoimet_suljetut = (
        ("avoimet", "Avoimet"),
        ("suljetut", "Suljetut"),
        ("kaikki", "Kaikki")
    )
    avoimet_vai_suljetut = forms.ChoiceField(choices=avoimet_suljetut, widget=forms.RadioSelect, required=False, initial="avoimet", label="")

    jarjestysVaihtoehdot = (
        ("asiakas", "Lainaaja"),
        ("varastonhoitaja", "Varastonhoitaja"),
        ("id", "ID"),
        ("tuoteryhma", "Tuoteryhmä"),
        ("tuote", "Tuote"),
        ("aikaleima", "Aikaleima"),
        ("viim_palautuspaiva", "Palautuspäivä"),
    )
    jarjestys = forms.ChoiceField(choices=jarjestysVaihtoehdot, label="Järjestys:", required=False, initial="asiakas")

    tavat = (
        ("nouseva", "Nouseva"),
        ("laskeva", "Laskeva"),
    )
    tapa = forms.ChoiceField(choices=tavat, widget=forms.RadioSelect, required=False, initial="nouseva", label="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['jarjestys'].widget.attrs.update({'class': 'rasekoblueborder roundedborder'})