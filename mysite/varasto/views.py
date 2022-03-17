from django.shortcuts import render

from django.http import HttpResponse, Http404

from django.shortcuts import get_object_or_404, render

from .models import Lainaus

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

def lainaukset(request):
    return HttpResponse(f"WORK IN PROGRESS")

def tyokalut(request):
    return HttpResponse(f"WORK IN PROGRESS")

# WIP
# Lainaukset tänään ... Lainaukset tällä viikolla ... 
# Vanhat lainaukset ... Lisää lainaus ... Lisää työkalu