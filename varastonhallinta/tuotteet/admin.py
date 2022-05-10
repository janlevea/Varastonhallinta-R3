from django.contrib import admin

from .models import Tuote, Tuoteryhma
from varasto.admin import ReadOnlyAdminMixin

class TuoteryhmaAdmin(admin.ModelAdmin):
    fields = (
        "lisaaja", "lisaysaika", "avoin", "poistaja", "poistoaika"
    )

    readonly_fields = ["lisaaja", "lisaysaika", "poistaja", "poistoaika"]

    list_display = (
        "nimi", "id", "avoin", "lisaaja", "lisaysaika"
    )

class TuoteAdmin(admin.ModelAdmin):
    fields = (
        "tuoteryhma", "nimike", "maara", "hankintapaikka", "kustannuspaikka",
        "viivakoodi_string", "lisaaja", "lisaysaika", "poistettu", "poistaja"
    )

    readonly_fields = [
        "tuoteryhma", "nimike", "maara",
        "hankintapaikka", "kustannuspaikka",
        "viivakoodi_string", 
        "lisaaja", "lisaysaika", 
        "poistettu", "poistaja"]

    list_display = (
        "nimike", "id", "tuoteryhma", "maara", "hankintapaikka", "poistettu"
    )
    pass

# class TuoteOldAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
#     list_display = (
#         "id", 
#         "tuoteryhma", "nimike", "maara",
#         "hankintapaikka", "kustannuspaikka",
#         "viivakoodi_string",
#         "lisaaja", "lisaysaika",
#         "poistaja", "poistettu"
#     )

admin.site.register(Tuoteryhma, TuoteryhmaAdmin)
admin.site.register(Tuote, TuoteAdmin)