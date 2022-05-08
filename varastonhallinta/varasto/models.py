from django.db import models

from kayttajat.models import Kayttaja
from tuotteet.models import Tuote
# from django.utils.translation import gettext_lazy as _

# UUID arkistotunnuksen luontia varten
import uuid

class VarastotapahtumaBase(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    arkistotunnus = models.UUIDField(
        default=uuid.uuid4, editable=False, null=False, blank=False, 
        unique=True, verbose_name="Arkistotunnus")

    tuote = models.ForeignKey(
        Tuote, null=False, on_delete=models.PROTECT, verbose_name="Tuote")
    maara = models.IntegerField(null=False, verbose_name="Määrä")

    aikaleima = models.DateTimeField(auto_now_add=True,
        null=False, editable=False, verbose_name="Aikaleima")
    palautuspaiva = models.DateField(
        null=False, verbose_name="Palautuspäivä")
    
    asiakas = models.ForeignKey(
        Kayttaja, null=False, on_delete=models.PROTECT, verbose_name="Asiakas",  related_name="asiakas")
    varastonhoitaja = models.ForeignKey(
        Kayttaja, null=False, on_delete=models.PROTECT, verbose_name="Varastonhoitaja", related_name="varastonhoitaja")
    
    class Meta:
        verbose_name = "Varastotapahtuma"
        verbose_name_plural = "Varastotapahtumat"
        abstract = True
        ordering = ['asiakas']
    def __str__(self):
        return f"id({self.id}) {self.tuote.nimike} {self.maara}kpl, Asiakas: {self.asiakas}, Varastonhoitaja: {self.varastonhoitaja}"

class Varastotapahtuma(VarastotapahtumaBase):
    pass

class VarastotapahtumaOld(VarastotapahtumaBase):
    asiakas = models.ForeignKey(
        Kayttaja, null=False, on_delete=models.PROTECT, verbose_name="Asiakas",  related_name="asiakas_oli")

    varastonhoitaja = models.ForeignKey(
        Kayttaja, null=False, on_delete=models.PROTECT, verbose_name="Varastonhoitaja", related_name="varastonhoitaja_oli")

    palautettu = models.DateTimeField(
        blank=True, null=True, editable=False, verbose_name="Palautettu")

    poistettu = models.DateTimeField(
        blank=True, null=True, editable=False, verbose_name="Poistettu")

    varastonhoitaja_poisto_palautus = models.ForeignKey(
        Kayttaja, null=False, on_delete=models.PROTECT, verbose_name="Varastonhoitaja poisto/palautus",  related_name="varastonhoitaja_poisto_palautus")

    class Meta(VarastotapahtumaBase.Meta):
        verbose_name = "Vanha varastotapahtuma"
        verbose_name_plural = "Vanhat varastotapahtumat"