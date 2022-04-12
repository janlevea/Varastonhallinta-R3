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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UusiLainaus(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            # cleaned_data = {
            #     "varastonhoitaja": form.cleaned_data["varastonhoitaja"],
            #     "asiakas": form.cleaned_data["asiakas"],
            #     "tuote": form.cleaned_data["tuote"],
            #     "maara": form.cleaned_data["maara"],
            #     "palautuspaiva": form.cleaned_data["palautuspaiva"],
            # }

            # TODO: form cleaning
            form.save()
            lainaus = Varastotapahtuma.objects.latest("id")
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