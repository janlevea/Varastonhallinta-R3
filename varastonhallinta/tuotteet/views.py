from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from tuotteet.models import Tuote, TuoteOld, Tuoteryhma
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
    queryset = Tuote.objects.all()
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

# Tuotteiden muokkaus.. Lowprio/unnecessary
# @login_required
# def muutaTuotetta(request, pk):
#     pass

@login_required
def poistaTuote(request, pk):
    tuote = get_object_or_404(Tuote, pk=pk)
    current_datetime = timezone.now()

    if request.method == 'POST':
        poistettuTuote = TuoteOld(
            id = tuote.id,
            tuoteryhma = tuote.tuoteryhma,
            nimike = tuote.nimike,
            maara = tuote.maara,
            hankintapaikka = tuote.hankintapaikka,
            kustannuspaikka = tuote.kustannuspaikka,
            tuotekuva = tuote.tuotekuva,
            viivakoodi_string = tuote.viivakoodi_string,
            viivakoodi_img = tuote.viivakoodi_img,
            lisaaja = tuote.lisaaja,
            lisaysaika = tuote.lisaysaika,

            poistaja = request.user,
            poistettu = current_datetime
        )
        poistettuTuote.save()
        tuote.delete()
        return redirect("../tuote_poistettu/")
    return render(request, "tuotteet/poista_tuote.html", {"tuote": tuote})

@login_required             
def tuotePoistettu(request):
    return render(request, "tuotteet/tuote_poistettu.html")

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
