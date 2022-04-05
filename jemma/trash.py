# views.py - deleted stuff

# index.html
# ilman renderiä
# from django.template import loader
# # Hae 5 viimeistä lainausta, viimeisin lainaus ensimmäisenä
# viimeisimmat_lainaukset = Lainaus.objects.order_by("-lainausaika")[:5]
# # Hae template
# template = loader.get_template("varasto/index.html")
# context = {
#     "viimeisimmat_lainaukset": viimeisimmat_lainaukset,
# }
# return HttpResponse(template.render(context, request))

# index.html
# ilman templatea:
# # Alusta tyhjä merkkijono johon lisätään lainaukset listasta
# string = ""
# # Käydään läpi lainaukset
# for lainaus in viimeisimmat_lainaukset:
#     # Jokainen lainaus omalle riville
#     string += f"{lainaus}<br>"
# # Palautetaan valmis sivu käyttäjälle nähtäväksi
# return HttpResponse(string)

# Lainaus ilman get_object_or_404 shortcuttia
# def lainaus(request, lainaus_id):
#     try:
#         laina = Lainaus.objects.get(pk=lainaus_id)
#     except Lainaus.DoesNotExist:
#         raise Http404(f"Lainausta({lainaus_id}) ei ole.")
#     return render(request, "varasto/lainaus.html", {"laina": laina})