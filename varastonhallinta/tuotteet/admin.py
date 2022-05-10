from django.contrib import admin

from .models import Tuote, Tuoteryhma
# from varasto.admin import ReadOnlyAdminMixin

class TuoteryhmaAdmin(admin.ModelAdmin):
    fields = (
        "nimi", "lisaaja", "lisaysaika", "avoin", "poistaja", "poistoaika"
    )

    readonly_fields = ["lisaysaika", "poistaja", "poistoaika"]

    list_display = (
        "nimi", "id", "avoin", "lisaaja", "lisaysaika"
    )
    list_filter = ("avoin",)
    ordering = ["nimi"]
# TODO: Suljetut tuoteryhmät erikseen

class TuoteAdmin(admin.ModelAdmin):
    fields = (
        "tuoteryhma", "nimike", "maara", "hankintapaikka", "kustannuspaikka",
        "viivakoodi_string", "lisaaja", "lisaysaika", "poistettu", "poistaja"
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