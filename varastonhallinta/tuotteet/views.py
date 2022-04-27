from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from tuotteet.models import Tuote

@login_required
def lista(request):
    queryset = Tuote.objects.all()
    tuotelista = {"object_list": queryset}
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
            return render(request, "tuotteet/tuote.html", {"lisays": lisaystapahtuma, "juuriLisatty": True})
        return render(request, "tuotteet/lisaa.html",
        {"form": form, "current_datetime": current_datetime})
    else:
        form = LisaaTuote()
    return render(request, "varasto/uusi_lainaus.html", {"form": form, "current_datetime": current_datetime})