from django.contrib import admin
from django.urls import include, path

from varastonhallinta.views import index

urlpatterns = [
    path('', index),
    path('varasto/', include('varasto.urls', namespace="varasto")),
    path('varasto/kayttajat/', include('kayttajat.urls', namespace="kayttajat")),
    path('varasto/tuotteet/', include('tuotteet.urls', namespace="tuotteet")),
    path('varasto/admin/', admin.site.urls),
] 

# TODO: Kaikki projektin urlsit muuttujiin? Templateissa paljon toistoa.