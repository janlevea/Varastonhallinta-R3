'''
views.py - poistettua

index.html
ilman renderiä
from django.template import loader
# Hae 5 viimeistä lainausta, viimeisin lainaus ensimmäisenä
viimeisimmat_lainaukset = Lainaus.objects.order_by("-lainausaika")[:5]
# Hae template
template = loader.get_template("varasto/index.html")
context = {
    "viimeisimmat_lainaukset": viimeisimmat_lainaukset,
}
return HttpResponse(template.render(context, request))

index.html
ilman templatea:
# Alusta tyhjä merkkijono johon lisätään lainaukset listasta
string = ""
# Käydään läpi lainaukset
for lainaus in viimeisimmat_lainaukset:
    # Jokainen lainaus omalle riville
    string += f"{lainaus}<br>"
# Palautetaan valmis sivu käyttäjälle nähtäväksi
return HttpResponse(string)

Lainaus ilman get_object_or_404 shortcuttia
def lainaus(request, lainaus_id):
    try:
        laina = Lainaus.objects.get(pk=lainaus_id)
    except Lainaus.DoesNotExist:
        raise Http404(f"Lainausta({lainaus_id}) ei ole.")
    return render(request, "varasto/lainaus.html", {"laina": laina})


Normi html-form - old - uusi_lainaus.html:stä
<form class="uusilainaus" method="POST">
    <label for="varastonhoitaja">Varastonhoitaja</label><br>
    <input type="text" id="varastonhoitaja" name="varastonhoitaja" required>
    <br>
    <label for="lainaaja">Lainaaja</label><br>
    <input type="text" id="lainaaja" name="lainaaja" required>
    <br><br>
    <label for="tuote">Tuote</label><br>
    <input type="text" id="tuote" name="tuote" required>
    <br>
    <label for="maara">Määrä</label><br>
    <input type="number" id="maara" name="maara" min="1" max="999" required>
    <br><br>
    <input type="submit" value="Lisää">
</form> 

viimeisimmät_lainaukset snippet html-templatessa käytettäväksi
{% if viimeisimmat_lainaukset %}
    <p>Viimeisimmät lainaukset:</p>
    <ul>
    {% for lainaus in viimeisimmat_lainaukset %}
        <li><a href="{% url 'lainaukset:lainaus' lainaus.id %}">
            {{lainaus.lainausaika}} - {{lainaus.tyokalu}} - {{lainaus.opiskelijanro}}
        </a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>Ei lainauksia näytettäväksi.</p>
{% endif %}

forms.py
Käsin tehty formi
class UusiLainaus(forms.Form):
    varastonhoitaja = forms.CharField(label="Varastonhoitaja", max_length=35, required=True)
    asiakas = forms.CharField(label="Asiakas", max_length=35, required=True)
    tuote = forms.CharField(label="Tuote", max_length=35, required=True)
    maara = forms.IntegerField(label="Määrä", required=True) # help_text="Kuinka monta?"
    aikaleima = forms.DateField(label="Aikaleima", required=True)
    palautuspaiva = forms.DateField(label="Palautuspäivä", required=True)

urls.py
varasto/1/
path("<int:pk>/", views.LainausView.as_view(), name="lainaus"),
varasto/lainaukset/
path("lainaukset/", views.LainauksetView.as_view(), name="lainaukset"),
varasto/tyokalut/
path("tyokalut/", views.TyokalutV

views.py

context_object_name = "viimeisimmat_lainaukset"

def get_queryset(self):
    # Return last 5 tool loans
    return Lainaus.objects.order_by('-lainausaika')

# Hae 5 viimeistä lainausta, viimeisin lainaus ensimmäisenä
viimeisimmat_lainaukset = Lainaus.objects.order_by("-lainausaika")[:5]
context = {
    "viimeisimmat_lainaukset": viimeisimmat_lainaukset,
}
return render(request, "varasto/index.html", context)

# vanhaa koodia
cleaned_data = {
    "varastonhoitaja": form.cleaned_data["varastonhoitaja"],
    "asiakas": form.cleaned_data["asiakas"],
    "tuote": form.cleaned_data["tuote"],
    "maara": form.cleaned_data["maara"],
    "palautuspaiva": form.cleaned_data["palautuspaiva"],
}
lainaus = Varastotapahtuma.objects.latest("id")
form.cleaned_data
form.save()
'''