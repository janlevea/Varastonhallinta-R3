from django.urls import path, include
from . import views
import django.contrib.auth.urls

app_name = "kayttajat"

urlpatterns = [
    path("", include(django.contrib.auth.urls)),
    path("profiili/<str:opiskelijanumero>/", views.profiili, name="profiili"),
    path("rekisteroidy/", views.rekisteroidy, name="rekisteroidy"),
    path("lista/", views.kayttajalista, name="kayttajalista"),
]