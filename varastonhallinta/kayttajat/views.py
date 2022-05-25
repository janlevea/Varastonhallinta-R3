from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from kayttajat.models import Kayttaja
from .forms import Rekisteroidy, KayttajaValinnat

@login_required
def profiili(request, opiskelijanumero):
    kayttaja = get_object_or_404(Kayttaja, opiskelijanumero=opiskelijanumero)
    return render(request, "kayttajat/profiili.html", {"user": kayttaja})

@login_required
def kayttajalista(request):
    # Hae käyttäjät, laskeva liittymisaika järjestys
    kayttajat = Kayttaja.objects.filter(aktiivinen=True).order_by("-liittynyt")
    # Alusta formit
    form = KayttajaValinnat()

    jarjestys = "Liittymisaika"
    valittuJarjestys = "liittynyt"
    tapa = "laskeva"
    merkki = "-"

    aktiiviset = "kylla"

    staffi = False
    admini = False

    if request.GET:
        form = KayttajaValinnat(request.GET)
        valittuJarjestys = request.GET['jarjestys']
        tapa = request.GET['tapa']
        aktiiviset = request.GET['aktiiviset']
        valinnat = request.GET.getlist('valinnat')

        if aktiiviset == "kylla":
            kayttajat = Kayttaja.objects.filter(aktiivinen=True)
        elif aktiiviset == "ei":
            kayttajat = Kayttaja.objects.filter(aktiivinen=False)
        else:
            kayttajat = Kayttaja.objects.all()

        if "staff" in valinnat:
            staffi = True
            kayttajat = kayttajat.filter(staff=True)

        if "admin" in valinnat:
            admini = True
            kayttajat = kayttajat.filter(admin=True)

        if tapa == "nouseva":
            merkki = ""
        elif tapa == "laskeva":
            merkki = "-"

        if valittuJarjestys == "liittynyt" or valittuJarjestys == "":
            jarjestys = "Liittymisaika"
            kayttajat = kayttajat.order_by(f"{merkki}liittynyt")

        elif valittuJarjestys == "opiskelijanumero":
            jarjestys = "Opiskelijanumero"
            kayttajat = kayttajat.order_by(f"{merkki}opiskelijanumero")

        elif valittuJarjestys == "etunimi":
            jarjestys = "Etunimi"
            kayttajat = kayttajat.order_by(f"{merkki}etunimi")

        elif valittuJarjestys == "sukunimi":
            jarjestys = "Sukunimi"
            kayttajat = kayttajat.order_by(f"{merkki}sukunimi")

        elif valittuJarjestys == "last_login":
            jarjestys = "Viimeisin kirjautuminen"
            kayttajat = kayttajat.order_by(f"{merkki}last_login")

    context = {
        "object_list": kayttajat,
        "form": form,
        "jarjestys": jarjestys,
        "tapa": tapa,
        "aktiiviset": aktiiviset,
        "staffi": staffi,
        "admini": admini,
    }

    return render(request, "kayttajat/kayttajat.html", context)

def rekisteroidy(request):
    if request.user.is_authenticated: # Jos käyttäjä on kirjautunut, ohjaa takas varaston etusivulle
        return redirect("/")

    if request.method == "POST":
        form = Rekisteroidy(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return render(request, "kayttajat/rekisterointi_onnistui.html")
    else:
        form = Rekisteroidy()
    return render(request, "kayttajat/rekisteroidy.html", {"form": form})