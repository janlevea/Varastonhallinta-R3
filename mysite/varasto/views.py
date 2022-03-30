from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Lainaus

class IndexView(generic.ListView):
    template_name = 'varasto/index.html'
    context_object_name = "viimeisimmat_lainaukset"
    
    def get_queryset(self):
        # Return last 5 tool loans
        return Lainaus.objects.order_by('-lainausaika')

class LainausView(generic.DetailView):
    model = Lainaus
    template_name = "varasto/lainaus.html"    

'''

# /varasto/ etusivu
def index(request):
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