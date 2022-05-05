from django.contrib import admin

from .models import Tuote, TuoteOld, Tuoteryhma
from varasto.admin import ReadOnlyAdminMixin

class TuoteOldAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = (
        "id", 
        "tuoteryhma", "nimike", "maara",
        "hankintapaikka", "kustannuspaikka",
        "viivakoodi_string",
        "lisaaja", "lisaysaika",
        "poistaja", "poistettu"
    )

admin.site.register(Tuoteryhma)
admin.site.register(Tuote)
admin.site.register(TuoteOld, TuoteOldAdmin)