from django.urls import path
from . import views

app_name = "tuotteet"

urlpatterns = [
    # tuotteet/lista.html
    path("lista/", views.lista, name="lista"),
    # tuotteet/tuote.html
    path("tuote/<int:pk>/", views.tuote, name="tuote"),
    # tuotteet/lisaa.html
    path("lisaa/", views.lisaa, name="lisaa"),
]