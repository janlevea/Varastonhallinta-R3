from django.db import models

from kayttajat.models import Kayttaja
from tuotteet.models import Tuote
# from django.utils.translation import gettext_lazy as _

# Importoi date/time-kirjastot käytettäväksi aikaleimoissa/palautuspäivässä
from datetime import timedelta
from django.utils import timezone

# UUID arkistotunnuksen luontia varten
import uuid

class Varastotapahtuma(models.Model):   
    id = models.AutoField(primary_key=True, null=False)
    arkistotunnus = models.CharField(
        default=uuid.uuid1(), editable=False, max_length=37, null=False, blank=False, unique=True, verbose_name="Arkistotunnus")

    tuote = models.ForeignKey(
        Tuote, null=False, on_delete=models.PROTECT, verbose_name="Tuote")
    maara = models.IntegerField(null=False, verbose_name="Määrä")

    aikaleima = models.DateTimeField(auto_now_add=True,
        null=False, editable=False, verbose_name="Aikaleima")
    palautuspaiva = models.DateField(
        null=False, default=(timezone.now() + timedelta(days=14)), verbose_name="Palautuspäivä")
    
    asiakas = models.ForeignKey(
        Kayttaja, null=False, related_name="asiakas", on_delete=models.PROTECT, verbose_name="Asiakas")
    varastonhoitaja = models.ForeignKey(
        Kayttaja, null=False, related_name="varastonhoitaja", on_delete=models.PROTECT, verbose_name="Varastonhoitaja")
    
    class Meta:
        verbose_name = "Varastotapahtuma"
        verbose_name_plural = "Varastotapahtumat"
    def __str__(self):
        return f"id({self.id}) {self.tuote.nimike} {self.maara}kpl, Asiakas: {self.asiakas}, Varastonhoitaja: {self.varastonhoitaja}"