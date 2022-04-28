from django import forms

from varasto.models import Varastotapahtuma

# Importoi date/time-kirjastot käytettäväksi aikaleimoissa/palautuspäivässä
from datetime import timedelta
from django.utils import timezone

# Varastotapahtuma modelista tehty formi uusi_lainaus -sivulle
class UusiLainaus(forms.ModelForm):

    palautuspaiva = forms.DateField(
        initial = (timezone.now() + timedelta(days=14))
    )
    
    class Meta:
        model = Varastotapahtuma
        fields = [
        "asiakas", 
        "tuote", "maara", 
        "palautuspaiva"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asiakas'].widget.attrs.update({'class': 'rasekoredborder roundedborder bottom-marg'})
        self.fields['tuote'].widget.attrs.update({'class': 'rasekoblueborder roundedborder'})
        self.fields['maara'].widget.attrs.update({'class': 'rasekoblueborder roundedborder bottom-marg'})
        self.fields['palautuspaiva'].widget.attrs.update({'class': 'blackborder roundedborder bottom-marg'})
        
# TODO: Tuote-valinnasta id pois