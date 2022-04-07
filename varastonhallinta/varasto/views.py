#from django.urls import reverse
#from django.views import generic
#from .models import Lainaus

from django.http import HttpResponseRedirect #, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
import datetime

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
    
def kirjauduUlos(request):
    return render(request, "varasto/kirjaudu_ulos.html")

def raportit(request):
    return render(request, "varasto/raportit.html")

def uusiLainaus(request):
    current_datetime = datetime.datetime.strftime(
        datetime.datetime.now(), "%d.%m.%Y %H:%M:%S")
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UusiLainaus(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            varastonhoitaja = form.cleaned_data["varastonhoitaja"]
            asiakas = form.cleaned_data["asiakas"]
            tuote = form.cleaned_data["tuote"]
            maara = form.cleaned_data["maara"]
            aikaleima = current_datetime
            palautuspaiva = form.cleaned_data["palautuspaiva"]
            return HttpResponseRedirect('/lisaa_lainaus/')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = UusiLainaus()

    return render(request, "varasto/uusi_lainaus.html", 
    {"form": form, "current_datetime": current_datetime})

def lainauksenPalautus(request):
    return render(request, "varasto/lainauksen_palautus.html")

# def lainaus(request, lainaus):
#     laina = get_object_or_404(Varastotapahtuma, pk=lainaus)
#     return render(request, "varasto/lainaus.html", {"laina": laina})

def lisaaMuokkaa(request):
    return render(request, "varasto/lisaa_muokkaa.html")

# class IndexView(generic.ListView):
#     template_name = "varasto/index.html"
#     def get_queryset(self):
#         return HttpResponse('varasto/index.html')
    '''
    context_object_name = "viimeisimmat_lainaukset"
    
    def get_queryset(self):
        # Return last 5 tool loans
        return Lainaus.objects.order_by('-lainausaika')

class LainausView(generic.DetailView):
    model = Lainaus
    template_name = "varasto/lainaus.html"    
    '''

# def raportit(request_iter):
#     return render(request_iter,'varasto/raportit.html')

# class RaportitView(generic.View):
#     template_name = "varasto/raportit.html"
#     def get_queryset(self):
#         return HttpResponse('varasto/raportit.html')
    

# /varasto/ etusivu
# def index(request):
#     pass

# def raportit(request):
#     pass

    '''
    # Hae 5 viimeistä lainausta, viimeisin lainaus ensimmäisenä
    viimeisimmat_lainaukset = Lainaus.objects.order_by("-lainausaika")[:5]
    context = {
        "viimeisimmat_lainaukset": viimeisimmat_lainaukset,
    }
    return render(request, "varasto/index.html", context)

def lainaus(request, lainaus_id):
    laina = get_object_or_404(Lainaus, pk=lainaus_id)
    return render(request, "varasto/lainaus.html", {"laina": laina})

# def poista(request, lainaus_id):
#     laina = get_object_or_404(Lainaus, pk=lainaus_id)
#     laina.delete(lainaus_id)
#     return HttpResponse("Lainaus", lainaus_id, "poistettu.")

def lainaukset(request):
    return HttpResponse(f"WORK IN PROGRESS")

def tyokalut(request):
    return HttpResponse(f"WORK IN PROGRESS")

# WIP
# Lainaukset tänään ... Lainaukset tällä viikolla ... 
# Vanhat lainaukset ... Lisää lainaus ... Lisää työkalu

'''