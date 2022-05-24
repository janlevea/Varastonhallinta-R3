from django.shortcuts import render, get_object_or_404 #, redirect
from django.utils import timezone # Aikaleimoja varten

from django.contrib.auth.decorators import login_required # Sivut vaativat kirjautumisen

from kayttajat.models import Kayttaja
from varasto.models import Varastotapahtuma
from .forms import UusiLainaus, PalautaLainaus, LainausJarjestys

@login_required
def index(request): # Varastonhallinnan etusivu
    return render(request, "varasto/index.html")

@login_required
def uusiLainaus(request):
    # Uuden lainauksen kirjaaminen
    current_datetime = timezone.now
    if request.method == 'POST':
        # POST - eli täytetty formi lähetettiin
        form = UusiLainaus(request.POST)
        if form.is_valid():
            # Formi on ok, luo varastotapahtuma
            lainaustapahtuma = Varastotapahtuma.objects.create(**form.cleaned_data,
            **{
                "varastonhoitaja": request.user, 
            })
            lainaustapahtuma.save()
            # Siirry lainauksen sivulle
            return render(request, "varasto/lainaus.html",  {"laina": lainaustapahtuma, "juuriLisatty": True})
    else:
        # EI POST - luo tyhjä lainausformi
        form = UusiLainaus()
    return render(request, "varasto/uusi_lainaus.html", 
    {"form": form, "current_datetime": current_datetime})

@login_required
def lainaus(request, pk):
    # Yksittäisen lainauksen sivu
    laina = get_object_or_404(Varastotapahtuma, pk=pk)
    return render(request, "varasto/lainaus.html", {"laina": laina, "juuriLisatty": False})

@login_required
def lainauksenPalautus(request): 
    current_datetime = timezone.now()
    form = PalautaLainaus()
    queryset = Varastotapahtuma.objects.avoimet()
    valittuAsiakas = ""
    if request.GET:
        form = PalautaLainaus(request.GET)
        valittuAsiakas = request.GET['asiakas']
        if not valittuAsiakas == "":
            valittuAsiakas = Kayttaja.objects.get(id=valittuAsiakas)
            # Näytä avoimet lainaukset lainaajan mukaan
            queryset = Varastotapahtuma.objects.filter(asiakas=valittuAsiakas, avoin=True)
        else:
            queryset = Varastotapahtuma.objects.avoimet()

    return render(request, "varasto/lainauksen_palautus.html",
    {"form": form, "current_datetime": current_datetime,
    "object_list": queryset, "asiakas": valittuAsiakas})

@login_required
def palautaLainaus(request, pk):
    laina = get_object_or_404(Varastotapahtuma, pk=pk)
    
    if request.method == 'POST': 
        # Varastonhoitaja painaa palauta_lainaus.html sivulla Kyllä nappulaa
        laina.avoin = False # Aseta laina suljetuksi
        laina.palautettu = timezone.now() # Palautuksen aikaleima
        laina.varastonhoitaja_palautus = request.user # Varastonhoitaja palautukselle
        laina.save() # Tallenna tietokantaan
        return render(request, "varasto/lainaus_palautettu.html", {"laina": laina}) # Vahvistussivu palautukselle - TODO: Näytä lainauksen tietoja tällä sivulla
    return render(request, "varasto/palauta_lainaus.html", {"laina": laina}) # Kyllä nappia ei ole painettu

@login_required
def lainaukset(request): # Lista kaikista avoimista lainauksista
    form = LainausJarjestys() # Lataa lainausten järjestysformi
    tapahtumat = Varastotapahtuma.objects.avoimet() # Lataa avoimet varastotapahtumat 
    queryset = tapahtumat.order_by("asiakas__etunimi") # Järjestä lainaukset valinnan mukaan
    jarjestys = "Lainaajan etunimi" # string joka kertoo valitun järjestyksen sivulla
    valittuJarjestys = "asiakas" # formista haettava järjestys (oletuksena lainaajan etunimi)
    tapa = "nouseva"
    merkki = "" # tyhjä on nouseva, "-" on laskeva
    if request.GET: # Järjestystä on vaihdettu
        form = LainausJarjestys(request.GET)
        valittuJarjestys = request.GET['jarjestys'] # Hae valittu järjestys form valinnasta
        tapa = request.GET['tapa'] # Nouseva vai laskeva?
        avoimet_vai_suljetut = request.GET['avoimet_vai_suljetut']

        if avoimet_vai_suljetut == "avoimet":
            tapahtumat = Varastotapahtuma.objects.avoimet()
        elif avoimet_vai_suljetut == "suljetut":
            tapahtumat = Varastotapahtuma.objects.suljetut()
        else:
            tapahtumat = Varastotapahtuma.objects.all()

        if tapa == "nouseva":
            merkki = ""
        elif tapa == "laskeva":
            merkki = "-"

        if valittuJarjestys == "asiakas" or valittuJarjestys == "": # asiakas/oletus valittu
            jarjestys = "Lainaajan etunimi"
            queryset = tapahtumat.order_by(f"{merkki}asiakas__etunimi")
        elif valittuJarjestys == "varastonhoitaja": # ...muut vaihtoehdot
            jarjestys = "Varastonhoitajan etunimi"
            queryset = tapahtumat.order_by(f"{merkki}varastonhoitaja__etunimi")
        elif valittuJarjestys == "id":
            jarjestys = "Lainauksen ID"
            queryset = tapahtumat.order_by(f"{merkki}id")
        elif valittuJarjestys == "tuoteryhma":
            jarjestys = "Tuoteryhmän nimi"
            queryset = tapahtumat.order_by(f"{merkki}tuote__tuoteryhma__nimi")
        elif valittuJarjestys == "tuote":
            jarjestys = "Tuotteen nimi"
            queryset = tapahtumat.order_by(f"{merkki}tuote__nimike")
        elif valittuJarjestys == "aikaleima":
            jarjestys = "Aikaleima/Lainausaika"
            queryset = tapahtumat.order_by(f"{merkki}aikaleima")
        elif valittuJarjestys == "viim_palautuspaiva":
            jarjestys = "Viimeinen palautuspäivä"
            queryset = tapahtumat.order_by(f"{merkki}viim_palautuspaiva")

    return render(request, "varasto/lainaukset.html", 
    {"object_list": queryset, "form": form, "jarjestys": jarjestys, "tapa": tapa, "avoimet_vai_suljetut": avoimet_vai_suljetut})