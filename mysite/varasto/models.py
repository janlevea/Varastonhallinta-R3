from django.db import models

# from django.utils.translation import gettext_lazy as _

class Varastotyyppi(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nimi = models.CharField(max_length=30, null=False)
    class Meta:
        verbose_name = "Varastotyyppi"
        verbose_name_plural = "Varastotyypit"
    def __str__(self):
        return f"ID: {self.id}, Nimi: {self.nimi}"

class Varasto(models.Model):
    id = models.CharField(max_length=20, null=False, primary_key=True)
    varastotyyppi = models.ForeignKey(Varastotyyppi, null=False, on_delete=models.PROTECT)
    nimi = models.CharField(max_length=30, null=False)
    class Meta:
        verbose_name = "Varasto"
        verbose_name_plural = "Varastot"
    def __str__(self):
        return f"ID: {self.id}, Tyyppi_ID: {self.varastotyyppi}, Nimi: {self.nimi}"

class Tuoteryhma(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nimi = models.CharField(max_length=50, null=False)
    class Meta:
        verbose_name = "Tuoteryhmä"
        verbose_name_plural = "Tuoteryhmät"
    def __str__(self):
        return f"ID: {self.id}, Nimi: {self.nimi}"

class Tuote(models.Model):
    viivakoodi = models.CharField(max_length=30, null=False, primary_key=True)
    id = models.IntegerField(null=False, default=1)
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

class Rooli(models.Model):
    roolinimitys = models.CharField(max_length=20, null=False, primary_key=True)
    class Meta:
        verbose_name = "Rooli"
        verbose_name_plural = "Roolit"
    def __str__(self):
        return f"Roolinimitys: {self.roolinimitys}"

class Henkilo(models.Model):
    id = models.CharField(max_length=50, null=False, primary_key=True)
    roolinimitys = models.ForeignKey(Rooli, max_length=20, null=False, on_delete=models.PROTECT)
    etunimi = models.CharField(max_length=35, null=False)
    class Meta:
        verbose_name = "Henkilö"
        verbose_name_plural = "Henkilöt"
    def __str__(self):
        return f"ID: {self.id}, Rooli: {self.roolinimitys}, Etunimi: {self.etunimi}"

class Varastotapahtuma(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    arkistotunnus = models.CharField(max_length=50, null=False)
    varasto = models.ForeignKey(Varasto, null=False, on_delete=models.PROTECT)
    viivakoodi = models.ForeignKey(Tuote, null=False, on_delete=models.PROTECT)
    maara = models.IntegerField(null=False)
    aikaleima = models.DateField(null=False)
    palautuspaiva = models.DateField(null=False)
    asiakas = models.ForeignKey(Henkilo, null=False, related_name="asiakas", on_delete=models.PROTECT)
    varastonhoitaja = models.ForeignKey(Henkilo, null=False, on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Varastotapahtuma"
        verbose_name_plural = "Varastotapahtumat"
    def __str__(self):
        return f"Viivakoodi: {self.viivakoodi}, Määrä: {self.maara}, Asiakas: {self.asiakas}, Varastonhoitaja: {self.varastonhoitaja}"

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
