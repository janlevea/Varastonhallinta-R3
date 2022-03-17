from django.db import models

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