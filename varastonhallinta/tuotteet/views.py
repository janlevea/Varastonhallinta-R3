from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from tuotteet.models import Tuote

@login_required
def lista(request):
    queryset = Tuote.objects.all()
    tuotelista = {"object_list": queryset}
    return render(request, "tuotteet/lista.html", tuotelista)

@login_required
def tuote(request, pk):
    tuote = get_object_or_404(Tuote, pk=pk)
    return render(request, "tuotteet/tuote.html", {"tuote": tuote})

@login_required
def lisaaMuokkaa(request):
    return render(request, "tuotteet/lisaa_muokkaa.html")