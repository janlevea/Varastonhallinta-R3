#from django.urls import reverse
#from django.views import generic
#from .models import Lainaus
# from http.client import HTTPResponse
# from django.http import HttpResponseRedirect #, HttpResponse, Http404

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from varasto.models import Varastotapahtuma

from .forms import UusiLainaus

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
    
# TODO: Login-sivu, @login_required...

def kirjauduUlos(request):
    return render(request, "varasto/kirjaudu_ulos.html")

def raportit(request):
    return render(request, "varasto/raportit.html")

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

def lainaus(request, pk):
    laina = get_object_or_404(Varastotapahtuma, pk=pk)
    return render(request, "varasto/lainaus.html", {"laina": laina})

def lisattyLainaus(request, pk):
    laina = get_object_or_404(Varastotapahtuma, pk=pk)
    return render(request, "varasto/lisatty_lainaus.html", {"laina": laina})

def lainauksenPalautus(request):
    return render(request, "varasto/lainauksen_palautus.html")

def lisaaMuokkaa(request):
    return render(request, "varasto/lisaa_muokkaa.html")

# def poista(request, lainaus_id):
#     laina = get_object_or_404(Lainaus, pk=lainaus_id)
#     laina.delete(lainaus_id)
#     return HttpResponse("Lainaus", lainaus_id, "poistettu.")