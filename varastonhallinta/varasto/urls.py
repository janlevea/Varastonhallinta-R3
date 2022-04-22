from django.urls import path, include

from . import views

app_name = "varasto"
urlpatterns = [
    # /varasto/ - etusivu
    path("", views.index, name="index"), 

    # /varasto/profiili/
    path("tili/", include("django.contrib.auth.urls")),
    path("profiili/<str:opiskelijanumero>/", views.profiili, name="profiili"),
    
    # Yksittäisten lainausten tiedot:
    # varasto/lainaus.html
    path("lainaus/<int:pk>/", views.lainaus, name="lainaus"),
    # varasto/lisatty_lainaus.html
    path("lisatty_lainaus/<int:pk>/", views.lisattyLainaus, name="lisattyLainaus"),
    # varasto/poista_lainaus.html
    path("poista_lainaus/<int:pk>", views.poistaLainaus, name="poistaLainaus"),
    # varasto/lainaus_poistettu.html
    path("lainaus_poistettu/", views.lainausPoistettu, name="lainausPoistettu"),

    # varasto/lainaukset.html - Kaikki avoimet lainaukset
    path("lainaukset/", views.lainaukset, name="lainaukset"),

    # varasto/raportit.html
    path("raportit/", views.raportit, name="raportit"),
    
    # varasto/uusi_lainaus.html
    path("uusi_lainaus/", views.uusiLainaus, name="uusiLainaus"),

    # varasto/lainauksen_palautus.html
    path("lainauksen_palautus/", views.lainauksenPalautus, name="lainauksenPalautus"),
    # varasto/lisaa_muokkaa.html
    path("lisaa_muokkaa/", views.lisaaMuokkaa, name="lisaaMuokkaa"),

    # varasto/tili/rekisteroidy
    path("tili/rekisteroidy/", views.rekisteroidy, name="rekisteroidy"),
    path("kayttajat/", views.kayttajat, name="kayttajat"),
]