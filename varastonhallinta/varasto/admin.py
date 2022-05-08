from django.contrib import admin

# Importoi modelit ja lisää ne näkymään admin-sivulla
from .models import Varastotapahtuma, VarastotapahtumaOld

# Importoi date/time-kirjastot käytettäväksi aikaleimoissa/palautuspäivässä
from datetime import timedelta
from django.utils import timezone

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
        "palautuspaiva",
        "asiakas", "varastonhoitaja"
    )

    #readonly_fields = ["arkistotunnus"]

    def get_changeform_initial_data(self, request):
        defPalautuspaiva = (timezone.now() + timedelta(days=14))
        return {
            "palautuspaiva": defPalautuspaiva,
            "varastonhoitaja": request.user
        }

    def save_model(self, request, obj, form, change):
        obj.varastonhoitaja = request.user
        super().save_model(request, obj, form, change)

class VarastotapahtumaOldAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = (
        "id", "arkistotunnus",
        "tuote", "maara",
        "aikaleima", "palautuspaiva",
        "asiakas", "varastonhoitaja",
        "varastonhoitaja_poisto_palautus", 
        "palautettu", "poistettu"
    )

admin.site.register(Varastotapahtuma, VarastotapahtumaAdmin)
admin.site.register(VarastotapahtumaOld, VarastotapahtumaOldAdmin)