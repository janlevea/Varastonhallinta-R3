from django.urls import path

from varasto import views

app_name = "varasto"
urlpatterns = [
    # /varasto/ - etusivu
    path("", views.index, name="index"), 
    
    # Yksittäisten lainausten tiedot:
    # varasto/lainaus.html
    path("lainaus/<int:pk>/", views.lainaus, name="lainaus"),

    # varasto/lainaukset.html - Kaikki avoimet lainaukset
    path("lainaukset/", views.lainaukset, name="lainaukset"),
    
    # varasto/uusi_lainaus.html
    path("uusi_lainaus/", views.uusiLainaus, name="uusiLainaus"),

    # varasto/lainauksen_palautus.html
    path("lainauksen_palautus/", views.lainauksenPalautus, name="lainauksenPalautus"),
    path("palauta_lainaus/<int:pk>", views.palautaLainaus, name="palautaLainaus"),
]