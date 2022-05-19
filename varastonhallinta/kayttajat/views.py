from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from kayttajat.models import Kayttaja
from .forms import Rekisteroidy, KayttajaJarjestys, KayttajaValinnat

@login_required
def profiili(request, opiskelijanumero):
    kayttaja = get_object_or_404(Kayttaja, opiskelijanumero=opiskelijanumero)
    return render(request, "kayttajat/profiili.html", {"user": kayttaja})

# TODO: Järjestysformit ei muista valintaa vaihtaessa
@login_required
def kayttajalista(request):
    # Hae käyttäjät, laskeva liittymisaika järjestys
    queryset = Kayttaja.objects.all().order_by("-liittynyt")
    # Alusta formit
    form = KayttajaJarjestys()
    formValinnat = KayttajaValinnat()

    jarjestys = "Liittymisaika"
    valittuJarjestys = "liittynyt"
    tapa = "laskeva"
    merkki = "-"

    if request.GET:
        form = KayttajaJarjestys(request.GET)
        formValinnat = KayttajaValinnat(request.GET)
        valittuJarjestys = request.GET['jarjestys']
        tapa = request.GET['tapa']
        aktiiviset = request.GET['aktiiviset']
        valinnat = request.GET.getlist('valinnat')

        queryset = queryset.filter(aktiivinen=aktiiviset)

        if "staff" in valinnat:
            queryset = queryset.filter(staff=True)

        if "admin" in valinnat:
            queryset = queryset.filter(admin=True)

        if tapa == "nouseva":
            merkki = ""
        elif tapa == "laskeva":
            merkki = "-"

        if valittuJarjestys == "liittynyt" or valittuJarjestys == "":
            jarjestys = "Liittymisaika"
            queryset = queryset.order_by(f"{merkki}liittynyt")

        elif valittuJarjestys == "opiskelijanumero":
            jarjestys = "Opiskelijanumero"
            queryset = queryset.order_by(f"{merkki}opiskelijanumero")

        elif valittuJarjestys == "etunimi":
            jarjestys = "Etunimi"
            queryset = queryset.order_by(f"{merkki}etunimi")

        elif valittuJarjestys == "sukunimi":
            jarjestys = "Sukunimi"
            queryset = queryset.order_by(f"{merkki}sukunimi")

        elif valittuJarjestys == "last_login":
            jarjestys = "Viimeisin kirjautuminen"
            queryset = queryset.order_by(f"{merkki}last_login")
    else:
        queryset = queryset.filter(aktiivinen=True)

    context = {
        "object_list": queryset,
        "form": form,
        "formValinnat": formValinnat,
        "jarjestys": jarjestys,
        "tapa": tapa,
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