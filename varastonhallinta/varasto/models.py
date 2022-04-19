from django.db import models
from django.contrib.auth.models import User

# from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Importoi date/time-kirjastot käytettäväksi aikaleimoissa/palautuspäivässä
from datetime import timedelta
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
    id = models.AutoField(primary_key=True, null=False)
    arkistotunnus = models.CharField(
        max_length=50, null=False, verbose_name="Arkistotunnus")
    varasto = models.ForeignKey(
        Varasto, null=False, on_delete=models.PROTECT, verbose_name="Varasto")
    tuote = models.ForeignKey(
        Tuote, null=False, on_delete=models.PROTECT, verbose_name="Tuote")
    maara = models.IntegerField(null=False, verbose_name="Määrä")
    aikaleima = models.DateTimeField(auto_now_add=True,
        null=False, editable=False, verbose_name="Aikaleima")
    palautuspaiva = models.DateField(
        null=False, default=(timezone.now() + timedelta(days=14)), verbose_name="Palautuspäivä")
    asiakas = models.ForeignKey(
        User, null=False, related_name="asiakas", on_delete=models.PROTECT, verbose_name="Asiakas")
    varastonhoitaja = models.ForeignKey(
        User, null=False, related_name="varastonhoitaja", on_delete=models.PROTECT, verbose_name="Varastonhoitaja")
    class Meta:
        verbose_name = "Varastotapahtuma"
        verbose_name_plural = "Varastotapahtumat"
    def __str__(self):
        return f"Määrä: {self.maara}, Asiakas: {self.asiakas}, Varastonhoitaja: {self.varastonhoitaja}"

class Profiili(models.Model):
    kayttaja = models.OneToOneField(User, on_delete=models.CASCADE)
    kuva = models.ImageField(default="oletus.jpg", upload_to="profiilikuvat")
    class Meta:
        verbose_name = "Profiili"
        verbose_name_plural = "Profiilit"
    def __str__(self):
        return self.kayttaja.username