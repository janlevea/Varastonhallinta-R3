from django.db import models

class Opiskelijat(models.Model):
    opiskelijanro = models.IntegerField(primary_key=True)
    etunimi = models.CharField(max_length=50)
    sukunimi = models.CharField(max_length=50)

    def __str__(self):
        return f"Opiskelija: {self.opiskelijanro} {self.etunimi} {self.sukunimi}"

class Tyokalut(models.Model):
    id = models.IntegerField(primary_key=True)
    nimi = models.CharField(max_length=60)

    def __str__(self):
        return f"Työkalu: {self.tyokalunro} {self.nimi}"

class Lainaukset(models.Model):
    id = models.IntegerField(primary_key=True)
    opiskelija = models.ForeignKey(Opiskelijat, on_delete=models.PROTECT)
    tyokalu = models.ForeignKey(Tyokalut, on_delete=models.PROTECT)
    lainausaika = models.DateTimeField()

    def __str__(self):
        return f"Lainaus {self.id}, Opiskelija {self.opiskelijanro}, Työkalu {self.tyokalunro}"