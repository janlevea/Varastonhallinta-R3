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
# TODO: Asiakkaan nimi näkyviin asiakas kenttään
# TODO: Tuote-valinnasta id pois