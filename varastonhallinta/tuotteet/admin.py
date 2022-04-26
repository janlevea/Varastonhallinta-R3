from django.contrib import admin

from .models import Tuote, Tuoteryhma

admin.site.register(Tuoteryhma)
admin.site.register(Tuote)