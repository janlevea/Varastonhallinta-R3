from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from tuotteet.models import Tuote, Tuoteryhma
from .forms import LisaaTuote, LisaaRyhma, ValitseRyhma

from stringToBCode import string2barcode

@login_required
def ryhmat(request):
    queryset = Tuoteryhma.objects.filter(poistettu = False)

    for i in queryset:
        i.tuotemaara = Tuote.objects.filter(tuoteryhma=i.id, poistettu = False).count()

    tuoteryhmat = {"object_list": queryset}
    return render(request, "tuotteet/ryhmat.html", tuoteryhmat)

@login_required
def ryhma(request, pk):
    tuoteryhma = get_object_or_404(Tuoteryhma, pk=pk)

    tuotteet = Tuote.objects.filter(tuoteryhma=pk, poistettu=False)
    tuoteryhma.tuotemaara = tuotteet.count()

    return render(request, "tuotteet/ryhma.html", {"tuoteryhma": tuoteryhma, "tuotteet": tuotteet, "naytanimi": False})

@login_required
def lista(request):
    form = ValitseRyhma()
    queryset = Tuote.objects.filter(poistettu = False)
    ryhma = ""
    if request.GET:
        form = ValitseRyhma(request.GET)
        valittuRyhmaId = request.GET['valittuRyhma']
        if valittuRyhmaId != "":
            queryset = Tuote.objects.filter(poistettu=False, tuoteryhma=valittuRyhmaId)
            ryhma = Tuoteryhma.objects.get(id=valittuRyhmaId)
        
    context = {"object_list": queryset, "naytanimi": True, "form": form, "ryhma": ryhma}
    return render(request, "tuotteet/lista.html", context)

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
                "lisaaja": request.user,
            })
            lisaystapahtuma.viivakoodi_encoded = string2barcode(lisaystapahtuma.viivakoodi_plaintxt, codeType="B")
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
    valittu_tuoteryhma = get_object_or_404(Tuoteryhma, pk=pk)

    if request.method == 'POST':
        tuotteet = Tuote.objects.filter(tuoteryhma=valittu_tuoteryhma)
        if tuotteet.count() > 0:
            return render(request, "tuotteet/poista_ryhma.html", {"tuoteryhma": valittu_tuoteryhma, "ryhmassaTuotteita": True})
        valittu_tuoteryhma.poistettu = True
        valittu_tuoteryhma.poistoaika = timezone.now()
        valittu_tuoteryhma.poistaja = request.user
        valittu_tuoteryhma.save()
        return render(request, "tuotteet/tuote_poistettu.html", {"ryhma": True}) # Vahvistussivu poistolle - TODO: Näytä ryhmän tiedot tällä sivulla
    return render(request, "tuotteet/poista_ryhma.html", {"tuoteryhma": valittu_tuoteryhma})

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


# '''
# temp: Tämä enkoodaa viivakoodi stringit ja tallentaa tietokantaan
# '''
# @login_required
# def enkoodaaViivakoodit(request):
#     '''
#     testistring = "A-0040-Z"
#     enkoodattu = string2barcode(testistring, codeType="B")
#     print(enkoodattu)
#     #enkoodattu = "ÌA-0040-ZÇÎ"
#     return render(request, "test.html", {"enkoodattu": enkoodattu})
#     '''

#     tuotteet = Tuote.objects.all()
#     for tuote in tuotteet:
#         tuote.viivakoodi_encoded = string2barcode(tuote.viivakoodi_plaintxt, codeType="B")
#         tuote.save()
#         print(tuote.viivakoodi_encoded)
#     print(tuotteet)
#     return HttpResponse(tuotteet)