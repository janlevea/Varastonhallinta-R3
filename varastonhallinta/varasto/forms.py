from django import forms

from varasto.models import Varastotapahtuma, User

# Varastotapahtuma modelista tehty formi uusi_lainaus -sivulle
class UusiLainaus(forms.ModelForm):
    class Meta:
        model = Varastotapahtuma
        fields = [
        "asiakas", 
        "varasto","tuote", "maara", 
        "palautuspaiva"]

class Rekisteroidy(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control'}), 
        label="Sähköposti", required=True)

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label="Salasana", required=True)

    password_repeat = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label="Vahvista salasana", required=True)

    class Meta:
        model = User
        fields = [
            "email", 
            "first_name", "last_name",
            "password", "password_repeat"
        ]