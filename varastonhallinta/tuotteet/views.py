from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from tuotteet.models import Tuote, Tuoteryhma
from .forms import LisaaTuote, LisaaRyhma

@login_required
def ryhmat(request):
    queryset = Tuoteryhma.objects.all()

    for i in queryset:
        i.maara = Tuote.objects.filter(tuoteryhma=i.id).count()

    tuoteryhmat = {"object_list": queryset}
    return render(request, "tuotteet/ryhmat.html", tuoteryhmat)

@login_required
def ryhma(request, pk):
    tuoteryhma = get_object_or_404(Tuoteryhma, pk=pk)

    tuotteet = Tuote.objects.filter(tuoteryhma=pk)
    tuoteryhma.tuotemaara = tuotteet.count()

    return render(request, "tuotteet/ryhma.html", {"tuoteryhma": tuoteryhma, "tuotteet": tuotteet, "naytanimi": False})

@login_required
def lista(request):
    queryset = Tuote.objects.filter(poistettu = False)
    tuotelista = {"object_list": queryset, "naytanimi": True}
    return render(request, "tuotteet/lista.html", tuotelista)

@login_required
def tuote(request, pk):
    tuote = get_object_or_404(Tuote, pk=pk)
    return render(request, "tuotteet/tuote.html", {"tuote": tuote})

@login_required
def lisaa(request):
    current_datetime = timezone.now

    if request.method == 'POST':
        form = LisaaTuote(request.POST)
        if form.is_valid():
            lisaystapahtuma = Tuote.objects.create(**form.cleaned_data,
            **{
                "lisaaja": request.user
            })
            lisaystapahtuma.save()
            return render(request, "tuotteet/tuote.html", {"tuote": lisaystapahtuma, "juuriLisatty": True})
        return render(request, "tuotteet/lisaa.html",
        {"form": form, "current_datetime": current_datetime})
    else:
        form = LisaaTuote()
    return render(request, "tuotteet/lisaa.html", {"form": form, "current_datetime": current_datetime})

@login_required
def poistaTuote(request, pk):
    tuote = get_object_or_404(Tuote, pk=pk)

    if request.method == 'POST':
        tuote.poistettu = True
        tuote.poistoaika = timezone.now()
        tuote.poistaja = request.user
        tuote.save()
        return render(request, "tuotteet/tuote_poistettu.html", {"ryhma": False}) # Vahvistussivu poistolle - TODO: Näytä tuotteen tietoja tällä sivulla
    return render(request, "tuotteet/poista_tuote.html", {"tuote": tuote})

@login_required
def poistaRyhma(request, pk):
    tuoteryhma = get_object_or_404(Tuoteryhma, pk=pk)
    tuotteet = tuoteryhma.objects.filter(Tuote)
    if request.method == 'POST':
        if tuotteet > 0:
            return render(request, "tuotteet/poista_ryhma.html", {"tuoteryhma": tuoteryhma})
        tuoteryhma.poistettu = True
        tuoteryhma.poistoaika = timezone.now()
        tuoteryhma.poistaja = request.user
        tuoteryhma.save()
        return render(request, "tuotteet/tuote_poistettu.html", {"ryhma": True}) # Vahvistussivu poistolle - TODO: Näytä ryhmän tiedot tällä sivulla
    return render(request, "tuotteet/poista_ryhma.html", {"tuoteryhma": tuoteryhma})

@login_required
def lisaaRyhma(request):
    current_datetime = timezone.now

    if request.method == 'POST':
        form = LisaaRyhma(request.POST)
        if form.is_valid():
            lisaystapahtuma = Tuoteryhma.objects.create(**form.cleaned_data,
            **{
                "lisaaja": request.user
            })
            lisaystapahtuma.save()
            return render(request, "tuotteet/ryhma.html", {"tuoteryhma": lisaystapahtuma, "juuriLisatty": True})
        return render(request, "tuotteet/lisaa_ryhma.html",
        {"form": form, "current_datetime": current_datetime})
    else:
        form = LisaaRyhma()
    return render(request, "tuotteet/lisaa_ryhma.html", {"form": form, "current_datetime": current_datetime})
