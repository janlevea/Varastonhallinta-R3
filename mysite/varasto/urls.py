from django.urls import path

from . import views

app_name = "lainaukset"
urlpatterns = [
    # /varasto/
    path('', views.IndexView.as_view(), name="index"), 
    # varasto/1/
    path("<int:pk>/", views.LainausView.as_view(), name="lainaus"),
    # varasto/1/poista/
    #path("<int:lainaus_id>/poista/", views.poista, name="poista"),
    # varasto/lainaukset/
    #path("lainaukset/", views.LainauksetView.as_view(), name="lainaukset"),
    # varasto/tyokalut/
    #path("tyokalut/", views.TyokalutView.as_view(), name="tyokalut")
]