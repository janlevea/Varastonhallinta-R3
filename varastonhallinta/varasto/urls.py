from django.urls import path

#from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

app_name = "varasto"
urlpatterns = [
    # /varasto/
    path("", views.index, name="index"), 

    # /varasto/profiili
    # path("profiili/<str:username>/", views.profiili, name="profiili"),

    # varasto/kirjaudu_ulos/
    path("kirjaudu_ulos/", views.kirjauduUlos, name="kirjauduUlos"),

    # varasto/lainaus.html
    path("lainaus/<int:pk>/", views.lainaus, name="lainaus"),
    # varasto/lisatty_lainaus.html
    path("lisatty_lainaus/<int:pk>/", views.lisattyLainaus, name="lisattyLainaus"),

    # varasto/raportit.html
    path("raportit/", views.raportit, name="raportit"),
    
    # varasto/uusi_lainaus.html
    path("uusi_lainaus/", views.uusiLainaus, name="uusiLainaus"),

    # varasto/lainauksen_palautus.html
    path("lainauksen_palautus/", views.lainauksenPalautus, name="lainauksenPalautus"),
    # varasto/lainauksen_palautus.html
    path("lisaa_muokkaa/", views.lisaaMuokkaa, name="lisaaMuokkaa"),

    # varasto/1/
    # path("<int:pk>/", views.LainausView.as_view(), name="lainaus"),
    # varasto/1/poista/
    #path("<int:lainaus_id>/poista/", views.poista, name="poista"),
    # varasto/lainaukset/
    #path("lainaukset/", views.LainauksetView.as_view(), name="lainaukset"),
    # varasto/tyokalut/
    #path("tyokalut/", views.TyokalutView.as_view(), name="tyokalut")
]