from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from tuotteet.models import Tuote, Tuoteryhma
from .forms import LisaaTuote, LisaaRyhma, TuoteValinnat, TuoteryhmaJarjestys

from stringToBCode import string2barcode

@login_required
def ryhmat(request):
    # Hae tuoteryhmät, laskeva lisäysaika järjestys, ei poistettuja
    ryhmat = Tuoteryhma.objects.filter(poistettu = False).order_by("-lisaysaika")
    # Alusta formi
    form = TuoteryhmaJarjestys()
    poistetut = "ei"
    jarjestys = "Lisäysaika"
    valittuJarjestys = "lisaysaika"
    tapa = "laskeva"
    merkki = "-"

    if request.GET:
        form = TuoteryhmaJarjestys(request.GET)
        poistetut = request.GET['poistetut']
        valittuJarjestys = request.GET['jarjestys']
        tapa = request.GET['tapa']

        if poistetut == "ei":
            ryhmat = Tuoteryhma.objects.filter(poistettu=False)
        elif poistetut == "kylla":
            ryhmat = Tuoteryhma.objects.filter(poistettu=True)
        else:
            ryhmat = Tuoteryhma.objects.all()

        if tapa == "nouseva":
            merkki = ""
        elif tapa == "laskeva":
            merkki = "-"

        if valittuJarjestys == "lisaysaika" or valittuJarjestys == "":
            jarjestys = "Lisäysaika"
            ryhmat = ryhmat.order_by(f"{merkki}lisaysaika")
        
        elif valittuJarjestys == "nimi":
            jarjestys = "Tuoteryhmän nimi"
            ryhmat = ryhmat.order_by(f"{merkki}nimi")

        elif valittuJarjestys == "lisaaja":
            jarjestys = "Ryhmän lisääjä"
            ryhmat = ryhmat.order_by(f"{merkki}lisaaja")

        elif valittuJarjestys == "id":
            jarjestys = "Ryhmän ID"
            ryhmat = ryhmat.order_by(f"{merkki}id")

    for i in ryhmat:
        i.tuotemaara = Tuote.objects.filter(tuoteryhma=i.id, poistettu = False).count()

    context = {
        "object_list": ryhmat, 
        "form": form, 
        "poistetut": poistetut, 
        "jarjestys": jarjestys, "tapa": tapa,
    }
    return render(request, "tuotteet/ryhmat.html", context)

@login_required
def ryhma(request, pk):
    tuoteryhma = get_object_or_404(Tuoteryhma, pk=pk)

    tuotteet = Tuote.objects.filter(tuoteryhma=pk, poistettu=False)
    tuoteryhma.tuotemaara = tuotteet.count()

    return render(request, "tuotteet/ryhma.html", {"tuoteryhma": tuoteryhma, "tuotteet": tuotteet, "naytanimi": False})

# TODO: Varastotilanteen katsominen etäältä

@login_required
def lista(request):
    form = TuoteValinnat()
    poistetut = "ei"
    jarjestys = "Tuotteen ID"
    valittuJarjestys = "id"
    tapa = "laskeva"
    merkki = "-"
    tuotteet = Tuote.objects.filter(poistettu = False)
    ryhma = ""

    if request.GET:
        form = TuoteValinnat(request.GET)
        poistetut = request.GET['poistetut']
        valittuRyhmaId = request.GET['valittuRyhma']
        valittuJarjestys = request.GET['jarjestys']
        tapa = request.GET['tapa']

        if poistetut == "ei":
            tuotteet = Tuote.objects.filter(poistettu=False)
        elif poistetut == "kylla":
            tuotteet = Tuote.objects.filter(poistettu=True)
        else:
            tuotteet = Tuote.objects.all()

        if tapa == "nouseva":
            merkki = ""
        elif tapa == "laskeva":
            merkki = "-"

        if valittuRyhmaId != "":
            tuotteet = tuotteet.filter(tuoteryhma=valittuRyhmaId)
            #queryset = Tuote.objects.filter(poistettu=False, tuoteryhma=valittuRyhmaId)
            ryhma = Tuoteryhma.objects.get(id=valittuRyhmaId)

        if valittuJarjestys == "id" or valittuJarjestys == "":
            jarjestys = "Tuotteen ID"   
            tuotteet = tuotteet.order_by(f"{merkki}id")   
        elif valittuJarjestys == "tuoteryhma":
            jarjestys = "Tuoteryhmän nimi"   
            tuotteet = tuotteet.order_by(f"{merkki}tuoteryhma__nimi")     
        elif valittuJarjestys == "nimike":
            jarjestys = "Tuotteen nimike"   
            tuotteet = tuotteet.order_by(f"{merkki}nimike") 
        elif valittuJarjestys == "hankintapaikka":
            jarjestys = "Hankintapaikka"   
            tuotteet = tuotteet.order_by(f"{merkki}hankintapaikka")
        elif valittuJarjestys == "kustannuspaikka":
            jarjestys = "Kustannuspaikka"   
            tuotteet = tuotteet.order_by(f"{merkki}kustannuspaikka")
        elif valittuJarjestys == "lisaaja":
            jarjestys = "Lisääjän nimi"   
            tuotteet = tuotteet.order_by(f"{merkki}lisaaja__nimi") 
        elif valittuJarjestys == "lisaysaika":
            jarjestys = "Tuotteen lisäysaika"   
            tuotteet = tuotteet.order_by(f"{merkki}lisaysaika")     

    context = {
        "object_list": tuotteet, 
        "poistetut": poistetut,
        "jarjestys": jarjestys,
        "tapa": tapa,
        "naytanimi": True, 
        "form": form, 
        "ryhma": ryhma
    }
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
        return render(request, "tuotteet/tuote_poistettu.html", {"ryhma": False}) # Vahvistussivu poistolle - # TODO: Näytä tuotteen tietoja tällä sivulla
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
        return render(request, "tuotteet/tuote_poistettu.html", {"ryhma": True}) # Vahvistussivu poistolle - # TODO: Näytä ryhmän tiedot tällä sivulla
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