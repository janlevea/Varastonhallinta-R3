from django.contrib import admin

from .models import Tuote, Tuoteryhma
# from varasto.admin import ReadOnlyAdminMixin

# TODO: enkoodatun viivakoodin luonti admintapahtumien yhteydessä
# from stringToBCode import string2barcode

class TuoteryhmaAdmin(admin.ModelAdmin):
    fields = (
        "nimi", "lisaaja", "lisaysaika", "poistettu", "poistaja", "poistoaika"
    )

    readonly_fields = ["lisaysaika", "poistaja", "poistoaika"]

    list_display = (
        "nimi", "id", "poistettu", "lisaaja", "lisaysaika"
    )
    list_filter = ("poistettu",)
    ordering = ["nimi"]
# TODO: Suljetut tuoteryhmät erikseen
# TODO: Tuotemäärä näkyviin tuoteryhmissä

class TuoteAdmin(admin.ModelAdmin):
    fields = (
        "tuoteryhma", "nimike", "maara", "hankintapaikka", "kustannuspaikka",
        "viivakoodi_plaintxt", "lisaaja", "lisaysaika", "poistettu", "poistaja"
    )

    readonly_fields = [
        "lisaysaika", 
        "poistettu", "poistaja"]

    list_display = (
        "nimike", "id", "tuoteryhma", "maara", "hankintapaikka", "poistettu"
    )
    list_filter =  ("poistettu",)
    ordering = ["nimike"]


# TODO: Poistetut tuotteet erikseen

admin.site.register(Tuoteryhma, TuoteryhmaAdmin)
admin.site.register(Tuote, TuoteAdmin)