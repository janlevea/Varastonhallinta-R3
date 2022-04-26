from django.urls import path

from . import views

app_name = "varasto"
urlpatterns = [
    # /varasto/ - etusivu
    path("", views.index, name="index"), 
    
    # Yksittäisten lainausten tiedot:
    # varasto/lainaus.html
    path("lainaus/<int:pk>/", views.lainaus, name="lainaus"),
    
    # varasto/lisatty_lainaus.html
    #path("lisatty_lainaus/<int:pk>/", views.lisattyLainaus, name="lisattyLainaus"),

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
]