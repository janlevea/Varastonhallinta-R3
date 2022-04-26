from django.contrib import admin

# Importoi modelit ja lisää ne näkymään admin-sivulla
from .models import Varastotapahtuma

admin.site.register(Varastotapahtuma)