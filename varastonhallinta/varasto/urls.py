from django.urls import path, include
#from django.conf.urls import url
#from django.views.generic.base import TemplateView

from . import views

app_name = "varasto"
urlpatterns = [
    # /varasto/ - etusivu
    path("", views.index, name="index"), 

    # /varasto/profiili - # TODO: Tee profiilisivu
    path("tili/", include("django.contrib.auth.urls")),
    path("profiili/", views.profiili, name="profiili"),
    # path("profiili/<str:username>/", views.profiili, name="profiili"),
    
    # Yksittäisten lainausten tiedot:
    # varasto/lainaus.html
    path("lainaus/<int:pk>/", views.lainaus, name="lainaus"),
    # varasto/lisatty_lainaus.html
    path("lisatty_lainaus/<int:pk>/", views.lisattyLainaus, name="lisattyLainaus"),
    # varasto/poista_lainaus.html
    path("poista_lainaus/<int:pk>", views.poistaLainaus, name="poistaLainaus"),
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
]