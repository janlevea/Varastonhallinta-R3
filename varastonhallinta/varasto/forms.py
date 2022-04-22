from django import forms

from varasto.models import Varastotapahtuma, Kayttaja

from django.contrib.auth.forms import ReadOnlyPasswordHashField

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
        model = Kayttaja
        fields = [
            "opiskelijanumero", "email", 
            "etunimi", "sukunimi",
            "password"
        ]

    def clean_password_repeat(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        password_repeat = self.cleaned_data.get("password_repeat")
        if password != password_repeat:
            raise forms.ValidationError("Salasanat eivät täsmää.")
        else:
            return password

    def clean_opiskelijanumero(self, *args, **kwargs):
        opiskelijanumero = self.cleaned_data.get("opiskelijanumero")
        if not opiskelijanumero.isdigit():
            raise forms.ValidationError("Opiskelijanumero voi sisältää vain numeroita.")
        elif not len(opiskelijanumero) == 5:
            raise forms.ValidationError("Opiskelijanumeron täytyy olla 5 merkkiä pitkä.")
        else:
            return opiskelijanumero


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    
    password = forms.CharField(label='Salasana', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Vahvista salasana', widget=forms.PasswordInput)

    class Meta:
        model = Kayttaja
        fields = [
            "opiskelijanumero", "email", 
            "etunimi", "sukunimi",
            "password"
        ]

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Salasanat eivät täsmää")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(label="Salasana")

    class Meta:
        model = Kayttaja
        fields = [
            'opiskelijanumero', 'email', 
            'etunimi', 'sukunimi',
            'password', 'aktiivinen', 'admin'
        ]

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]