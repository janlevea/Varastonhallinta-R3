#from django.urls import reverse
#from django.views import generic
#from .models import Lainaus
# from http.client import HTTPResponse
# from django.http import HttpResponseRedirect #, HttpResponse, Http404

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.contrib.auth.decorators import login_required
# from django.contrib import messages

from varasto.models import Varasto, Varastotapahtuma, User
from .forms import UusiLainaus

@login_required
def index(request):
    return render(request, "varasto/index.html")

# def profiili(request, username=None):
#     if username:
#         post_owner = get_object_or_404(User, username=username)
#     else:
#         post_owner = request.user

#     username = {
#         'post_owner': post_owner,
#     }
#     return render(request, "varasto/profiili.html")

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
            lainaus = Varastotapahtuma.objects.create(**form.cleaned_data, **{"varastonhoitaja": request.user})
            lainaus.save()
            return redirect("../lisatty_lainaus/" + str(lainaus.id))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UusiLainaus()
    return render(request, "varasto/uusi_lainaus.html", 
    {"form": form, "current_datetime": current_datetime})

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
    return render(request, "varasto/lainauksen_palautus.html")

@login_required
def lisaaMuokkaa(request):
    return render(request, "varasto/lisaa_muokkaa.html")

@login_required
def profiili(request, username):
    kayttaja = get_object_or_404(User, username=username)
    return render(request, "varasto/profiili.html", {"kayttaja": kayttaja})

'''
def profiili(request):
if request.method == 'POST':
    form = MuutaProfiilia(request.POST, request.FILES, instance=request.user)

    if form.is_valid():
        form.save()
        messages.success(request, 'Profiilikuva päivitetty.')
        return redirect(to='profiili')
else:
    form = MuutaProfiilia()
return render(request, 'varasto/profiili.html', {'form': form})
'''