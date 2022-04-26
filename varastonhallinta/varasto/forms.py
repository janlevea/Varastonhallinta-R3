from django import forms

from varasto.models import Varastotapahtuma

# Varastotapahtuma modelista tehty formi uusi_lainaus -sivulle
class UusiLainaus(forms.ModelForm):
    class Meta:
        model = Varastotapahtuma
        fields = [
        "asiakas", 
        "tuote", "maara", 
        "palautuspaiva"]
# TODO: Asiakkaan nimi näkyviin asiakas kenttään
# TODO: Tuote-valinnasta id pois