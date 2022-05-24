from django.contrib import admin

from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .forms import UserAdminCreationForm, UserAdminChangeForm
# from django.contrib.auth.models import Group

Kayttaja = get_user_model()

class AktiivinenFilter(SimpleListFilter):
    title = _('Aktiivinen')
    parameter_name = 'aktiivinen'

    def lookups(self, request, model_admin):
        return (
            (None, _("Kyllä")),
            ("ei", _("Ei")),
            ("kaikki", _("Kaikki"))
        )

    def choices(self, cl):
        for (lookup, title) in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': cl.get_query_string({
                    self.parameter_name: lookup,
                }, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        value = self.value()
        if value is None:
            return queryset.filter(aktiivinen=True)
        elif value == 'ei':
            return queryset.filter(aktiivinen=False)
        return queryset

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    add_form_template='admin/admin_lisaa_kayttaja.html'

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['opiskelijanumero', 'sukunimi', 'etunimi', 'admin']
    list_filter = ['admin', 'staff', AktiivinenFilter]

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