from django.contrib import admin

from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy as _

from .models import Tuote, Tuoteryhma
# from varasto.admin import ReadOnlyAdminMixin

from stringToBCode import string2barcode

class PoistettuFilter(SimpleListFilter):
    title = _('Poistettu')
    parameter_name = 'poistettu'

    def lookups(self, request, model_admin):
        return (
            (None, _("Ei")),
            ("kylla", _("Kyllä")),
            ("kaikki", _("Kaikki"))
        )

    def choices(self, cl):
        for (lookup, title) in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': cl.get_query_string({
                    self.parameter_name: lookup,
                }, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        value = self.value()
        if value is None:
            return queryset.filter(poistettu=False)
        elif value == 'kylla':
            return queryset.filter(poistettu=True)
        return queryset

class TuoteryhmaAdmin(admin.ModelAdmin):
    fields = (
        "nimi", "lisaaja", "lisaysaika", "poistettu", "poistaja", "poistoaika"
    )

    readonly_fields = ["lisaysaika", "poistaja", "poistoaika"]

    list_display = (
        "nimi", "id", "poistettu", "lisaaja", "lisaysaika"
    )
    list_filter = [PoistettuFilter]
    ordering = ["nimi"]
    
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
    list_filter = [PoistettuFilter]
    ordering = ["nimike"]

    def save_model(self, request, obj, form, change):
        obj.viivakoodi_encoded = string2barcode(obj.viivakoodi_plaintxt, codeType="B")
        super().save_model(request, obj, form, change)

admin.site.register(Tuoteryhma, TuoteryhmaAdmin)
admin.site.register(Tuote, TuoteAdmin)