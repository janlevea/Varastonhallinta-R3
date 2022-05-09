from django.shortcuts import render, get_object_or_404 #, redirect
from django.utils import timezone # Aikaleimoja varten

from django.contrib.auth.decorators import login_required # Sivut vaativat kirjautumisen

from varasto.models import Varastotapahtuma
from .forms import UusiLainaus, PalautaLainaus

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

    if request.method == 'POST':
        form = PalautaLainaus(request.POST)
        if form.is_valid():
            # Näytä avoimet lainaukset lainaajan mukaan
            asiakas1 = form.cleaned_data["asiakas"]
            queryset = Varastotapahtuma.objects.filter(asiakas=asiakas1, avoin=True)
            return render(request, "varasto/lainauksen_palautus.html", 
            {"current_datetime": current_datetime, 
            "object_list": queryset, "asiakas": asiakas1})
    else:
        # Lainaajaa ei ole valittu
        form = PalautaLainaus()

    return render(request, "varasto/lainauksen_palautus.html",
    {"form": form, "current_datetime": current_datetime})

@login_required
def palautaLainaus(request, pk):
    laina = get_object_or_404(Varastotapahtuma, pk=pk)
    
    if request.method == 'POST': 
        # Varastonhoitaja painaa palauta_lainaus.html sivulla Kyllä nappulaa
        laina.avoin = False # Aseta laina suljetuksi
        laina.palautettu = timezone.now() # Palautuksen aikaleima
        laina.varastonhoitaja_palautus = request.user # Varastonhoitaja palautukselle
        laina.save() # Tallenna tietokantaan
        return render(request, "varasto/lainaus_palautettu.html") # Vahvistussivu palautukselle - TODO: Näytä lainauksen tietoja tällä sivulla
    return render(request, "varasto/palauta_lainaus.html", {"laina": laina}) # Kyllä nappia ei ole painettu

@login_required
def lainaukset(request): # Lista kaikista avoimista lainauksista
    queryset = Varastotapahtuma.objects.filter(avoin = True)
    return render(request, "varasto/lainaukset.html", {"object_list": queryset})

# TODO: Vanhat/Palautetut lainaukset