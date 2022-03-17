from django.urls import path

from . import views

app_name = "lainaukset"
urlpatterns = [
    # /varasto/
    path('', views.index, name="index"), 
    # varasto/1/
    path("<int:lainaus_id>/", views.lainaus, name="lainaus"),
    # varasto/lainaukset/
    path("lainaukset/", views.lainaukset, name="lainaukset"),
    # varasto/tyokalut/
    path("tyokalut/", views.tyokalut, name="tyokalut")
]