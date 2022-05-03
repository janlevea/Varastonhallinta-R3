from django.contrib import admin

# Importoi modelit ja lisää ne näkymään admin-sivulla
from .models import Varastotapahtuma

# Importoi date/time-kirjastot käytettäväksi aikaleimoissa/palautuspäivässä
from datetime import timedelta
from django.utils import timezone

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

admin.site.register(Varastotapahtuma, VarastotapahtumaAdmin)