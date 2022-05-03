from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.contrib.auth.decorators import login_required

from varasto.models import Varastotapahtuma
from .forms import UusiLainaus, PalautaLainaus

@login_required
def index(request):
    return render(request, "varasto/index.html")

@login_required
def raportit(request):
    return render(request, "varasto/raportit.html")

@login_required
def uusiLainaus(request):
    current_datetime = timezone.now
    # if POST request - process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UusiLainaus(request.POST)
        # check whether it's valid:
        if form.is_valid():
            lainaustapahtuma = Varastotapahtuma.objects.create(**form.cleaned_data,
            **{
                "varastonhoitaja": request.user, 
            })
            lainaustapahtuma.save()
            return render(request, "varasto/lainaus.html",  {"laina": lainaustapahtuma, "juuriLisatty": True})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UusiLainaus()
    return render(request, "varasto/uusi_lainaus.html", 
    {"form": form, "current_datetime": current_datetime})

@login_required
def lainaus(request, pk):
    laina = get_object_or_404(Varastotapahtuma, pk=pk)
    return render(request, "varasto/lainaus.html", {"laina": laina, "juuriLisatty": False})

@login_required
def poistaLainaus(request, pk):
    laina = get_object_or_404(Varastotapahtuma, pk=pk)
    if request.method == 'POST':
        laina.delete()
        return redirect("../lainaus_poistettu/")
    return render(request, "varasto/poista_lainaus.html", {"laina": laina})

@login_required
def lainausPoistettu(request):
    return render(request, "varasto/lainaus_poistettu.html")

@login_required
def lainaukset(request):
    queryset = Varastotapahtuma.objects.all()
    lainaukset = {"object_list": queryset}
    return render(request, "varasto/lainaukset.html", lainaukset)

@login_required
def lainauksenPalautus(request):
    current_datetime = timezone.now

    if request.method == 'POST':
        form = PalautaLainaus(request.POST)
        if form.is_valid():
            asiakas1 = form.cleaned_data["asiakas"]
            queryset = Varastotapahtuma.objects.filter(asiakas=asiakas1)
            return render(request, "varasto/lainauksen_palautus.html", 
            {"current_datetime": current_datetime, 
            "object_list": queryset, "asiakas": asiakas1})
    else:
        form = PalautaLainaus()

    return render(request, "varasto/lainauksen_palautus.html",
    {"form": form, "current_datetime": current_datetime})