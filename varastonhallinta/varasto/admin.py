from django.contrib import admin

from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy as _

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

# class AvoinFilter(SimpleListFilter):
#     title = _('Avoin')
#     parameter_name = 'avoin'

#     def lookups(self, request, model_admin):
#         return (
#             (None, "Avoimet"),
#             ()
#         )

class VarastotapahtumaAdmin(admin.ModelAdmin):
    fields = [
        #"arkistotunnus",
        ("tuote", "maara"),
        "viim_palautuspaiva",
        "asiakas", "varastonhoitaja",
        "avoin"
    ]

    # Kentät fieldsetteinä
    # fieldsets = (
    #     ("", {
    #         "fields": ("tuote", "maara",),
    #     }),
    #     ("", {
    #         "fields": ("viim_palautuspaiva",),
    #     }),
    #     ("", {
    #         "fields": ("asiakas", "varastonhoitaja",),
    #     }),
    #     ("", {
    #         "fields": ("avoin",),
    #     })
    # )

    list_display = (
        "tuote", "maara", "id", "asiakas", "avoin", "viim_palautuspaiva"
    )
    list_filter = ("avoin",)

    # TODO: AvoinFilter
    # list_filter = [AvoinFilter] 
    # https://github.com/Raision-seudun-koulutuskuntayhtyma/todo-app2/blob/main/tehtavat/admin.py

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