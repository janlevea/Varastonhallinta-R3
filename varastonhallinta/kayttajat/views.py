from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from kayttajat.models import Kayttaja
from .forms import Rekisteroidy

@login_required
def profiili(request, opiskelijanumero):
    kayttaja = get_object_or_404(Kayttaja, opiskelijanumero=opiskelijanumero)
    return render(request, "kayttajat/profiili.html", {"user": kayttaja})

@login_required
def kayttajalista(request):
    queryset = Kayttaja.objects.order_by("opiskelijanumero")
    kayttajalista = {"object_list": queryset}
    return render(request, "kayttajat/kayttajat.html", kayttajalista)

def rekisteroidy(request):
    if request.user.is_authenticated: # Jos käyttäjä on kirjautunut, ohjaa takas varaston etusivulle
        return redirect("/")

    if request.method == "POST":
        form = Rekisteroidy(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect("/varasto/kayttajat/login/")
    else:
        form = Rekisteroidy()
    return render(request, "kayttajat/rekisteroidy.html", {"form": form})