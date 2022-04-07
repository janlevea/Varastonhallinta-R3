from django.db import models
from django.contrib.auth.models import User
# from django.utils.translation import gettext_lazy as _

from datetime import datetime, timedelta
from django.utils import timezone

class Varasto(models.Model):
    id = models.CharField(max_length=20, null=False, primary_key=True)
    varastotyyppi = models.CharField(max_length=30, null=False)
    nimi = models.CharField(max_length=30, null=False)
    class Meta:
        verbose_name = "Varasto"
        verbose_name_plural = "Varastot"
    def __str__(self):
        return f"ID: {self.id}, Tyyppi: {self.varastotyyppi}, Nimi: {self.nimi}"

class Tuoteryhma(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nimi = models.CharField(max_length=50, null=False)
    class Meta:
        verbose_name = "Tuoteryhmä"
        verbose_name_plural = "Tuoteryhmät"
    def __str__(self):
        return f"ID: {self.id}, Nimi: {self.nimi}"

class Tuote(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    viivakoodi = models.CharField(max_length=30, null=False)
    tuoteryhma = models.ForeignKey(Tuoteryhma, null=False, on_delete=models.PROTECT)
    nimike = models.CharField(max_length=50, null=False)
    hankintapaikka = models.CharField(max_length=50, null=False)
    kustannuspaikka = models.CharField(max_length=10, null=False)
    tuotekuva = models.BinaryField(null=False)
    class Meta:
        verbose_name = "Tuote"
        verbose_name_plural = "Tuotteet"
    def __str__(self):
        return f"Tuote_ID: {self.id}, Tuoteryhma_ID: {self.tuoteryhma}, Nimike: {self.nimike}"

class Varastotapahtuma(models.Model):
    datetime_current = datetime.now()

    arkistotunnus = models.CharField(
        primary_key=True, max_length=50, null=False, verbose_name="Arkistotunnus")
    varasto = models.ForeignKey(
        Varasto, null=False, on_delete=models.PROTECT, verbose_name="Varasto")
    tuote = models.ForeignKey(
        Tuote, null=False, on_delete=models.PROTECT, verbose_name="Tuote")
    maara = models.IntegerField(null=False, verbose_name="Määrä")
    aikaleima = models.DateField(
        null=False, default=timezone.now(), editable=False, verbose_name="Aikaleima")
    palautuspaiva = models.DateField(
        null=False, default=datetime_current + timedelta(days=14), verbose_name="Palautuspäivä")
    asiakas = models.ForeignKey(
        User, null=False, related_name="asiakas", on_delete=models.PROTECT, verbose_name="Asiakas")
    varastonhoitaja = models.ForeignKey(
        User, null=False, related_name="varastonhoitaja", on_delete=models.PROTECT, verbose_name="Varastonhoitaja")
    class Meta:
        verbose_name = "Varastotapahtuma"
        verbose_name_plural = "Varastotapahtumat"
    def __str__(self):
        return f"Määrä: {self.maara}, Asiakas: {self.asiakas}, Varastonhoitaja: {self.varastonhoitaja}"

'''
Käyttöön djangon käyttäjät tämän modelin sijaan
class Henkilo(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    roolinimitys = models.CharField(max_length=20, null=False, choices=(('opettaja', 'Opettaja'), ('oppilas', 'Oppilas')), default="oppilas")
    etunimi = models.CharField(max_length=35, null=False)
    sukunimi = models.CharField(max_length=35, null=False)
    class Meta:
        verbose_name = "Henkilö"
        verbose_name_plural = "Henkilöt"
    def __str__(self):
        return f"ID: {self.id}, Rooli: {self.roolinimitys}, Nimi: {self.etunimi} {self.sukunimi}"
'''


''' Vanha koodi:
class Opiskelija(models.Model):
    opiskelijanro = models.IntegerField(primary_key=True)
    etunimi = models.CharField(max_length=50)
    sukunimi = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Opiskelija"
        verbose_name_plural = "Opiskelijat"

    def __str__(self):
        return f"{self.opiskelijanro} {self.etunimi} {self.sukunimi}"

class Tyokalu(models.Model):
    id = models.AutoField(primary_key=True)
    nimi = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Työkalu"
        verbose_name_plural = "Työkalut"

    def __str__(self):
        return f"{self.id} {self.nimi}"

class Lainaus(models.Model):
    id = models.AutoField(primary_key=True)
    opiskelijanro = models.ForeignKey(Opiskelija, on_delete=models.PROTECT)
    tyokalu = models.ForeignKey(Tyokalu, on_delete=models.PROTECT)
    lainausaika = models.DateTimeField()
    class Meta:
        verbose_name = "Lainaus"
        verbose_name_plural = "Lainaukset"

    def __str__(self):
        return f"Lainaus: {self.id}, Opiskelija: {self.opiskelijanro}, Työkalu: {self.tyokalu}, Lainausaika: {self.lainausaika}"
'''
