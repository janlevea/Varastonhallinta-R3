from django.urls import path, include
from . import views
import django.contrib.auth.urls

app_name = "kayttajat"

urlpatterns = [
    # kayttajat/auth_urls
    path("", include(django.contrib.auth.urls)),
    
    # kayttajat/profiili/<opiskelijanumero>/
    path("profiili/<str:opiskelijanumero>/", views.profiili, name="profiili"),

    # kayttajat/rekisteroidy/
    path("rekisteroidy/", views.rekisteroidy, name="rekisteroidy"),

    # kayttajat/lista/
    path("lista/", views.kayttajalista, name="kayttajalista"),
]