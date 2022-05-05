from django.urls import path
from . import views

app_name = "tuotteet"

urlpatterns = [
    # tuotteet/ryhmat.html
    path("ryhmat/", views.ryhmat, name="ryhmat"),
    # tuotteet/ryhma.html
    path("ryhma/<int:pk>/", views.ryhma, name="ryhma"),
    # tuotteet/lisaa_ryhma.html
    path("lisaa_ryhma/", views.lisaaRyhma, name="lisaaRyhma"),

    # tuotteet/lista.html
    path("lista/", views.lista, name="lista"),
    # tuotteet/tuote.html
    path("tuote/<int:pk>/", views.tuote, name="tuote"),
    # tuotteet/lisaa.html
    path("lisaa/", views.lisaa, name="lisaa"),
    # tuotteet/poista_tuote.html
    path("poista_tuote/<int:pk>", views.poistaTuote, name="poistaTuote"),
    path("tuote_poistettu/", views.tuotePoistettu, name="tuotePoistettu"),
]