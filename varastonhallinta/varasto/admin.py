from django.contrib import admin

from .models import Varasto, Tuoteryhma, Tuote, Varastotapahtuma

admin.site.register(Varasto)
admin.site.register(Tuoteryhma)
admin.site.register(Tuote)
admin.site.register(Varastotapahtuma)
