from django.db import models

from kayttajat.models import Kayttaja
from tuotteet.models import Tuote

# from django.utils.translation import gettext_lazy as _

# UUID arkistotunnuksen luontia varten
import uuid

class Varastotapahtuma(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, editable=False, unique=True)

    arkistotunnus = models.UUIDField(
        default=uuid.uuid4, editable=False, null=False, blank=False, 
        unique=True, verbose_name="Arkistotunnus") # Uniikki arkistotunnus jokaiselle varastotapahtumalle

    tuote = models.ForeignKey(
        Tuote, null=False, blank=False, on_delete=models.PROTECT, verbose_name="Tuote") # Viittaus lainattuun tuotteeseen
    maara = models.IntegerField(null=False, blank=False, verbose_name="Määrä") # Tuotteen lukumäärä

    aikaleima = models.DateTimeField(auto_now_add=True,
        null=False, blank=False, editable=False, verbose_name="Aikaleima") # Lainauksen aika
    viim_palautuspaiva = models.DateField(
        null=False, blank=False, verbose_name="Viim. palautuspäivä") # Merkitty viimeinen palautuspäivä
    
    asiakas = models.ForeignKey(
        Kayttaja, null=False, blank=False, on_delete=models.PROTECT, 
        verbose_name="Asiakas", related_name="asiakas") # Lainaaja
    varastonhoitaja = models.ForeignKey(
        Kayttaja, null=False, blank=False, editable=False, on_delete=models.PROTECT, 
        verbose_name="Varastonhoitaja", related_name="varastonhoitaja") # Lainauksen kirjaaja
    
    avoin = models.BooleanField(
        null=False, blank=False, default=True, verbose_name="Avoin") # avoin=True, jos lainausta ei ole palautettu
    palautettu = models.DateTimeField(
        blank=True, null=True, editable=False, verbose_name="Palautettu") # Palautuksen aikaleima
    varastonhoitaja_palautus = models.ForeignKey(
        Kayttaja, null=True, blank=True, on_delete=models.PROTECT, 
        verbose_name="Palautuksen varastonhoitaja", related_name="varastonhoitaja_palautus") # Varastonhoitaja joka kirjasi palautuksen

    class Meta:
        verbose_name = "Varastotapahtuma"
        verbose_name_plural = "Varastotapahtumat"
        ordering = ['asiakas'] # Varastotapahtumat järjestellään oletuksena asiakkaan mukaan
    def __str__(self):
        return f"id({self.id}) {self.tuote.nimike} {self.maara}kpl, Asiakas: {self.asiakas}, Varastonhoitaja: {self.varastonhoitaja}"

# TODO: VarastotapahtumaQuerySet kuntoon
# class VarastotapahtumaQuerySet(models.QuerySet):
#     # Varastotapahtuma.objects.avoimet()
#     def avoimet(self):
#         return self.filter(avoin = True)

#     # Varastotapahtuma.objects.suljetut()
#     def suljetut(self):
#         return self.filter(avoin = False)