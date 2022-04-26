from django.urls import path
from . import views

app_name = "tuotteet"

urlpatterns = [
    # tuotteet/lisaa_muokkaa/
    path("lisaa_muokkaa/", views.lisaaMuokkaa, name="lisaaMuokkaa"), # TODO: Onko tarpeellinen? Lisää/Muokkaa toiminnallisuus voi olla /lista/ & /tuote/ sivulla
    # tuotteet/lista/
    path("lista/", views.lista, name="lista"),
    # varasto/tuote.html
    path("tuote/<int:pk>/", views.tuote, name="tuote"),
]