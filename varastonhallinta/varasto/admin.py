from django.contrib import admin

# Importoi modelit ja lisää ne näkymään admin-sivulla
from .models import Varastotapahtuma

# Importoi date/time-kirjastot käytettäväksi aikaleimoissa/palautuspäivässä
from datetime import timedelta
from django.utils import timezone

from django.contrib.auth.models import Group

admin.site.unregister(Group)

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
        "tuote", "maara", "id", "asiakas", "avoin", "viim_palautuspaiva"
    )
    list_filter = ("avoin",)

    # search_fields = [""] - TODO: haku käyttöön
    ordering = ["asiakas"]

    def get_changeform_initial_data(self, request):
        defPalautuspaiva = (timezone.now() + timedelta(days=14))
        return {
            "viim_palautuspaiva": defPalautuspaiva,
            "varastonhoitaja": request.user
        }

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

# TODO: Avoimet/suljetut varastotapahtumat erikseen

admin.site.register(Varastotapahtuma, VarastotapahtumaAdmin)