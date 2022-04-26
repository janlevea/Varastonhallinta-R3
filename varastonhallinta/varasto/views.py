from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.contrib.auth.decorators import login_required

from varasto.models import Varastotapahtuma
from .forms import UusiLainaus

# UUID arkistotunnuksen luontia varten
import uuid

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
            lainaus = Varastotapahtuma.objects.create(**form.cleaned_data,
            **{
                "varastonhoitaja": request.user, 
                "arkistotunnus": uuid.uuid1()
            })
            lainaus.save()
            return redirect("../lisatty_lainaus/" + str(lainaus.id))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UusiLainaus()
    return render(request, "varasto/uusi_lainaus.html", 
    {"form": form, "current_datetime": current_datetime})
# TODO: "/lisatty_lainaus" -> /lainaus/<pk>, ei tarvitse 2 viewiä. Contextissa voi kertoa lainauksen olevan uusi
# (juuriLisatty = True)

@login_required
def lainaus(request, pk):
    laina = get_object_or_404(Varastotapahtuma, pk=pk)
    return render(request, "varasto/lainaus.html", {"laina": laina})

@login_required
def lisattyLainaus(request, pk):
    laina = get_object_or_404(Varastotapahtuma, pk=pk)
    return render(request, "varasto/lisatty_lainaus.html", {"laina": laina})

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
    return render(request, "varasto/lainauksen_palautus.html", {"current_datetime": current_datetime})