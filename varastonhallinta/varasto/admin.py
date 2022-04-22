from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth import get_user_model

from .forms import UserAdminCreationForm, UserAdminChangeForm

# Importoi modelit ja lisää ne näkymään admin-sivulla
from .models import Varasto, Tuoteryhma, Tuote, Varastotapahtuma

Kayttaja = get_user_model()

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    add_form_template='varasto/admin_lisaa_kayttaja.html'

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['opiskelijanumero', 'admin']
    list_filter = ['admin', 'staff', 'aktiivinen']

    fieldsets = (
        (None, {'fields': ('email', 'password', 'liittynyt')}),
        ('Henkilötiedot', {'fields': ('etunimi', 'sukunimi')}),
        ('Oikeudet', {'fields': ('admin', 'staff', 'aktiivinen')}),
    )
    readonly_fields = ['liittynyt']

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
        'classes': ('wide',),
        'fields': ('opiskelijanumero', 'email', 'password', 'password_2')}),
        ('Henkilötiedot', {'fields': ('etunimi', 'sukunimi')}),
        ('Oikeudet', {'fields': ('admin', 'staff', 'aktiivinen')}),
    )

    search_fields = ['opiskelijanumero', 'email', 'etunimi', 'sukunimi']
    ordering = ['opiskelijanumero']
    filter_horizontal = ()

admin.site.register(Kayttaja, UserAdmin)

admin.site.register(Varasto)
admin.site.register(Tuoteryhma)
admin.site.register(Tuote)
admin.site.register(Varastotapahtuma)