from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .forms import UserAdminCreationForm, UserAdminChangeForm
# from django.contrib.auth.models import Group

Kayttaja = get_user_model()

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    add_form_template='kayttajat/admin_lisaa_kayttaja.html'

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['opiskelijanumero', 'sukunimi', 'etunimi', 'admin']
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