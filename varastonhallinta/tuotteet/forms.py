from django import forms

from tuotteet.models import Tuote, Tuoteryhma, TuoteryhmaNimiMaara

class LisaaTuote(forms.ModelForm):
    class Meta:
        model = Tuote
        fields = [
            "tuoteryhma",
            "nimike", "maara",
            "hankintapaikka", "kustannuspaikka",
            "viivakoodi_plaintxt"
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['tuoteryhma'].widget.attrs.update({'class': 'roundedborder rasekoredborder'})
        self.fields['nimike'].widget.attrs.update({'class': 'roundedborder rasekoredborder'})
        self.fields['maara'].widget.attrs.update({'class': 'roundedborder rasekoredborder bottom-marg'})
        self.fields['hankintapaikka'].widget.attrs.update({'class': 'roundedborder rasekoblueborder'})
        self.fields['kustannuspaikka'].widget.attrs.update({'class': 'roundedborder rasekoblueborder bottom-marg'})
        self.fields['viivakoodi_plaintxt'].widget.attrs.update({'class': 'roundedborder blackborder'})

class LisaaRyhma(forms.ModelForm):
    class Meta:
        model = Tuoteryhma
        fields = [
            "nimi"
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['nimi'].label = "Tuoteryhmän nimi"
        self.fields['nimi'].widget.attrs.update({'class': 'roundedborder rasekoredborder'})

# järjestäminen, poistettu/poistoaika/poistaja, lisääjä/lisäysaika
class TuoteValinnat(forms.Form):
    poistettu_valinta = (
        ("ei", "Ei"),
        ("kylla", "Kyllä"),
        ("kaikki", "Kaikki")
    )
    poistetut = forms.ChoiceField(
        choices=poistettu_valinta,
        widget=forms.RadioSelect, required=False,
        initial="ei", label="Poistetut")

    # TODO: Order_by: tuotemäärä -> nimi
    queryset = TuoteryhmaNimiMaara.objects.all().order_by("nimi")
    valittuRyhma = forms.ModelChoiceField(queryset=queryset, label="Ryhmä:", required=False, empty_label="Kaikki")

    ######
    jarjestysVaihtoehdot = (
        ("id", "ID"),
        ("tuoteryhma", "Tuoteryhmä"),
        ("nimike", "Nimike"),
        ("hankintapaikka", "Hankintapaikka"),
        ("kustannuspaikka", "Kustannuspaikka"),
        ("lisaaja", "Lisääjä"),
        ("lisaysaika", "Lisäysaika")
    )
    jarjestys = forms.ChoiceField(choices=jarjestysVaihtoehdot, label="Järjestys:", required=False, initial="id")

    tavat = (
        ("nouseva", "Nouseva"),
        ("laskeva", "Laskeva"),
    )
    tapa = forms.ChoiceField(choices=tavat, widget=forms.RadioSelect, required=False, initial="nouseva", label="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['valittuRyhma'].widget.attrs.update({'class': 'rasekoblueborder roundedborder'})
        self.fields['jarjestys'].widget.attrs.update({'class': 'rasekoblueborder roundedborder'})

class TuoteryhmaJarjestys(forms.Form):
    poistettu_valinta = (
        ("ei", "Ei"),
        ("kylla", "Kyllä"),
        ("kaikki", "Kaikki")
    )
    poistetut = forms.ChoiceField(
        choices=poistettu_valinta,
        widget=forms.RadioSelect, required=False,
        initial="ei", label="Poistetut")

    jarjestysVaihtoehdot = (
        ("lisaysaika", "Lisäysaika"),
        ("nimi", "Nimi"),
        ("lisaaja", "Lisääjä"),
        ("id", "ID"),
        # ("tuotemaara", "Tuotemäärä")
    )
    jarjestys = forms.ChoiceField(
        choices = jarjestysVaihtoehdot,
        label = "Järjestys:",
        required = False,
        initial = "lisaysaika",
    )

    tavat = (
        ("nouseva", "Nouseva"),
        ("laskeva", "Laskeva"),
    )
    tapa = forms.ChoiceField(
        choices=tavat, 
        widget=forms.RadioSelect, 
        required=False, 
        initial="laskeva", 
        label=""
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['jarjestys'].widget.attrs.update({'class': 'rasekoblueborder roundedborder'})

##### Varmaan tarpeeton:
# class MuutaTuotetta(forms.ModelForm):
#     class Meta:
#         model = Tuote
#         fields = [
#             "tuoteryhma", "nimike", "maara",
#             "hankintapaikka", "kustannuspaikka",
#             "tuotekuva", "viivakoodi_plaintxt"
#         ]