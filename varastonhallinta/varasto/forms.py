from django import forms

from varasto.models import Varastotapahtuma

# Importoi date/time-kirjastot käytettäväksi aikaleimoissa/palautuspäivässä
from datetime import timedelta
from django.utils import timezone

# Varastotapahtuma modelista tehty formi uusi_lainaus -sivulle
class UusiLainaus(forms.ModelForm):
    viim_palautuspaiva = forms.DateField(
        initial = (timezone.now() + timedelta(days=14))
    ) # Alusta oletuksena viim_palautuspaiva 14-päivän päähän
    
    class Meta:
        model = Varastotapahtuma
        fields = [
            # Tarpeelliset kentät
            "asiakas", 
            "tuote", "maara", 
            "viim_palautuspaiva"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aseta css-luokkia formin tyylittelyä varten
        self.fields['asiakas'].widget.attrs.update({'class': 'rasekoredborder roundedborder bottom-marg'})
        self.fields['tuote'].widget.attrs.update({'class': 'rasekoblueborder roundedborder'})
        self.fields['maara'].widget.attrs.update({'class': 'rasekoblueborder roundedborder bottom-marg'})
        self.fields['viim_palautuspaiva'].widget.attrs.update({'class': 'blackborder roundedborder bottom-marg'})        
    # TODO: Tuote-valinnasta id pois

class PalautaLainaus(forms.ModelForm):
    class Meta:
        model = Varastotapahtuma
        fields = [
            # Etsi lainauksia asiakkaan mukaan
            "asiakas"
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO: Näytä vain asiakkaat joilla on avoimia lainauksia
        #self.fields['asiakas'].queryset = Varastotapahtuma.objects.filter(Varastotapahtuma.asiakas)
        self.fields['asiakas'].widget.attrs.update({'class': 'rasekoredborder roundedborder bottom-marg'})