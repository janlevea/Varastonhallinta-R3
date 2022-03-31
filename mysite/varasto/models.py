from django.db import models

class Varastotyyppi(models.model):
    varastotyyppi_id = models.AutoField(primary_key=True, null=False)
    varastotyyppi_nimi = models.CharField(max_length=30, null=False)
    class Meta:
        verbose_name = "Varastotyyppi"
        verbose_name_plural = "Varastotyypit"
    def __str__(self):
        return f"ID: {self.varastotyyppi_id}, Nimi: {self.varastotyyppi_nimi}"

class Varasto(models.model):
    varasto_id = models.CharField(max_length=20, null=False, primary_key=True)
    varastotyyppi_id = models.ForeignKey(Varastotyyppi, null=False, on_delete=models.PROTECT)
    varaston_nimi = models.CharField(max_length=30, null=False)
    class Meta:
        verbose_name = "Varasto"
        verbose_name_plural = "Varastot"
    def __str__(self):
        return f"ID: {self.varasto_id}, Tyyppi_ID: {self.varastotyyppi_id}, Nimi: {self.varaston_nimi}"

class Tuoteryhma(models.model):
    tuoteryhma_id = models.AutoField(primary_key=True, null=False)
    tuoteryhma_nimi = models.CharField(max_length=50, null=False)
    class Meta:
        verbose_name = "Tuoteryhmä"
        verbose_name_plural = "Tuoteryhmät"
    def __str__(self):
        return f"ID: {self.tuoteryhma_id}, Nimi: {self.tuoteryhma_nimi}"

class Tuote(models.model):
    viivakoodi = models.CharField(max_length=30, null=False, primary_key=True)
    tuote_id = models.AutoField(null=False)
    tuoteryhma_id = models.ForeignKey(Tuoteryhma, null=False, on_delete=models.PROTECT)
    nimike = models.CharField(max_length=50, null=False)
    hankintapaikka = models.CharField(max_length=50, null=False)
    kustannuspaikka = models.CharField(max_length=10, null=False)
    tuotekuva = models.BinaryField(null=False)
    class Meta:
        verbose_name = "Tuote"
        verbose_name_plural = "Tuotteet"
    def __str__(self):
        return f"Tuote_ID: {self.tuote_id}, Tuoteryhma_ID: {self.tuoteryhma_id}, Nimike: {self.nimike}"

class Rooli(models.model):
    roolinimitys = models.CharField(max_length=20, null=False, primary_key=True)
    class Meta:
        verbose_name = "Rooli"
        verbose_name_plural = "Roolit"
    def __str__(self):
        return f"Roolinimitys: {self.roolinimitys}"

class Henkilo(models.model):
    henkilo_id = models.CharField(max_length=50, null=False, primary_key=True)
    roolinimitys = models.ForeignKey(Rooli, max_length=20, null=False, on_delete=models.PROTECT)
    etunimi = models.CharField(max_length=35, null=False)
    class Meta:
        verbose_name = "Henkilö"
        verbose_name_plural = "Henkilöt"
    def __str__(self):
        return f"ID: {self.henkilo_id}, Rooli: {self.roolinimitys}, Etunimi: {self.etunimi}"

class Varastotapahtuma(models.model):
    tapahtuma_id = models.AutoField(primary_key=True, null=False)
    arkistotunnus = models.CharField(max_length=50, null=False)
    varasto_id = models.ForeignKey(Varasto, null=False, on_delete=models.PROTECT)
    viivakoodi = models.ForeignKey(Tuote, null=False, on_delete=models.PROTECT)
    maara = models.IntegerField(null=False)
    aikaleima = models.DateField(null=False)
    palautuspaiva = models.DateField(null=False)
    asiakas_id = models.ForeignKey(Henkilo, null=False, on_delete=models.PROTECT)
    varastonhoitaja_id = models.ForeignKey(Henkilo, null=False, on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Varastotapahtuma"
        verbose_name_plural = "Varastotapahtumat"
    def __str__(self):
        return f"Viivakoodi: {self.viivakoodi}, Määrä: {self.maara}, Asiakas: {self.asiakas_id}, Varastonhoitaja: {self.varastonhoitaja_id}"

'''
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