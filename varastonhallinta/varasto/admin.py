from django.contrib import admin

# Importoi modelit ja lisää ne näkymään admin-sivulla
from .models import Varastotapahtuma

# Importoi date/time-kirjastot käytettäväksi aikaleimoissa/palautuspäivässä
from datetime import timedelta
from django.utils import timezone

# Tee admin-sivusta "ReadOnly" (estä muutokset)
class ReadOnlyAdminMixin:
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class VarastotapahtumaAdmin(admin.ModelAdmin):
    fields = (
        #"arkistotunnus",
        "tuote", "maara",
        "viim_palautuspaiva",
        "asiakas", "varastonhoitaja",
        "avoin"
    )

    list_display = (
        "avoin", "id", "tuote", "maara", "viim_palautuspaiva",
        "asiakas",
    )
    # TODO: viim. palautuspäivä näkyy listassa 23. toukokuuta 2022 -> 23.5.2022 parempi

    readonly_fields = ["asiakas", "varastonhoitaja", "avoin"]

    def get_changeform_initial_data(self, request):
        defPalautuspaiva = (timezone.now() + timedelta(days=14))
        return {
            "viim_palautuspaiva": defPalautuspaiva,
        }

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

# TODO: Avoimet/suljetut varastotapahtumat eri admin sivuilla

# class SuljettuVarastotapahtumaAdmin(admin.ModelAdmin):
#     list_display = (
#         "id", "arkistotunnus",
#         "tuote", "maara",
#         "aikaleima", "viim_palautuspaiva",
#         "asiakas", "varastonhoitaja",
#         "palautettu", "varastonhoitaja_palautus" 
#     )

admin.site.register(Varastotapahtuma, VarastotapahtumaAdmin)
#admin.site.register(Varastotapahtuma, SuljettuVarastotapahtumaAdmin)