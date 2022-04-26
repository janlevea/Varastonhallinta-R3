from django.contrib import admin

# Importoi modelit ja lisää ne näkymään admin-sivulla
from .models import Tuoteryhma, Tuote, Varastotapahtuma

admin.site.register(Tuoteryhma)
admin.site.register(Tuote)
admin.site.register(Varastotapahtuma)