from django import forms

from varasto.models import Varastotapahtuma

# Varastotapahtuma modelista tehty formi uusi_lainaus -sivulle
class UusiLainaus(forms.ModelForm):
    class Meta:
        model = Varastotapahtuma
        fields = [
        "asiakas", 
        "varasto","tuote", "maara", 
        "palautuspaiva"]